"""Typed parser for the deliberately small Phase-A frozen language."""

from __future__ import annotations

import re
from dataclasses import dataclass

import sympy as sp


class ParseError(ValueError):
    """A value is outside the frozen language."""


@dataclass(frozen=True)
class Domain:
    dimensions: tuple[tuple[str, str], ...]

    @property
    def cardinality(self) -> sp.Expr:
        result = sp.Integer(1)
        for name, rule in self.dimensions:
            if rule == "0..N**2-1":
                result *= sp.Symbol("N", nonzero=True) ** 2
            elif rule == "0..3":
                result *= 4
            elif rule == "0<=mu<nu<=3":
                result *= 6
            else:
                raise ParseError(f"unsupported index rule for {name}: {rule}")
        return sp.expand(result)


def _tokens(text: str) -> list[str]:
    tokens = re.findall(r"\*\*|[A-Za-z_][A-Za-z_0-9]*|\d+|[()+,=*/\-]", text)
    if "".join(tokens) != re.sub(r"\s+", "", text):
        raise ParseError("invalid token in frozen expression")
    return tokens


def component_rule(text: str) -> Domain:
    if text == "single":
        return Domain(())
    if text in {"mu=0..3", "mu=0..2"}:
        return Domain((("mu", text.split("=")[1]),))
    if text == "0<=mu<nu<=3":
        return Domain((("mu,nu", "0<=mu<nu<=3"),))
    raise ParseError(f"unsupported component rule: {text}")


def descriptor(text: str) -> Domain:
    compact = text.replace(" ", "")
    if re.fullmatch(r"[SPA VT]+\[A=0\.\.N\*\*2-1\]", compact):
        return Domain((("A", "0..N**2-1"),))
    if re.fullmatch(r"[VA]\[mu=0\.\.3,A=0\.\.N\*\*2-1\]", compact):
        return Domain((("mu", "0..3"), ("A", "0..N**2-1")))
    if re.fullmatch(r"T\[0<=mu<nu<=3,A=0\.\.N\*\*2-1\]", compact):
        return Domain((("mu,nu", "0<=mu<nu<=3"), ("A", "0..N**2-1")))
    raise ParseError(f"unsupported component descriptor: {text}")


def parse_metric(values: list[str]) -> tuple[sp.Integer, ...]:
    if len(values) != 4 or any(value not in {"1", "-1"} for value in values):
        raise ParseError("unsupported metric signature")
    return tuple(sp.Integer(value) for value in values)


def parse_trace_normalization(text: str) -> sp.Integer:
    if "".join(_tokens(text)) != "trace(Id4)=4":
        raise ParseError("unsupported Dirac trace normalization")
    return sp.Integer(4)


def parse_generator_normalization(text: str) -> tuple[sp.Integer, Domain]:
    if "".join(_tokens(text)) != "trace(lam(A)*lam(B))=2*KroneckerDelta(A,B)":
        raise ParseError("unsupported U(N) generator normalization")
    return sp.Integer(2), Domain((("A", "0..N**2-1"),))


def parse_grassmann_sign(text: str) -> sp.Integer:
    if "".join(_tokens(text)) not in {"-1", "1"}:
        raise ParseError("invalid grassmann crossing sign")
    return sp.Integer(text)


def expand_basis_expression(
    text: str, domain: Domain, gammas: list[sp.Matrix], gamma5: sp.Matrix
) -> list[sp.Matrix]:
    compact = "".join(_tokens(text))
    if domain.dimensions == ():
        if compact == "Id4":
            return [sp.eye(4)]
        if compact == "gamma5":
            return [gamma5]
    if (
        len(domain.dimensions) == 1
        and domain.dimensions[0][0] == "mu"
        and domain.dimensions[0][1] in {"0..3", "0..2"}
    ):
        count = int(domain.dimensions[0][1][-1]) + 1
        if compact == "gamma(mu)":
            return list(gammas[:count])
        if compact == "I*gamma(mu)*gamma5":
            return [sp.I * item * gamma5 for item in gammas[:count]]
        if compact == "gamma(mu)*gamma5":
            return [item * gamma5 for item in gammas[:count]]
    if (
        domain.dimensions == (("mu,nu", "0<=mu<nu<=3"),)
        and compact == "I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2"
    ):
        return [
            sp.I * (gammas[mu] * gammas[nu] - gammas[nu] * gammas[mu]) / 2
            for mu in range(4)
            for nu in range(mu + 1, 4)
        ]
    raise ParseError(f"basis expression/domain mismatch: {text}")


def canonical_operator(text: str) -> str:
    compact = "".join(_tokens(text))
    allowed = {
        "Sum",
        "bilinear",
        "lam",
        "Id4",
        "IdN",
        "gamma",
        "gamma5",
        "I",
        "G",
        "N",
        "A",
        "mu",
        "d",
    }
    names = set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*", compact))
    if names - allowed:
        raise ParseError(f"outside frozen vocabulary: {sorted(names - allowed)}")
    if compact.count("(") != compact.count(")"):
        raise ParseError("unbalanced frozen operator expression")
    return compact
