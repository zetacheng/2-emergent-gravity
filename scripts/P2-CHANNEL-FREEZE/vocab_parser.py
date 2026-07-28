"""Typed recursive-descent parser for the Phase-A frozen language.

Only scalar leaves lower to SymPy.  Dirac/internal operators, bilinears and
bound sums remain typed AST nodes throughout verification.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import sympy as sp


class ParseError(ValueError):
    """A value is outside the frozen grammar."""


@dataclass(frozen=True)
class Number:
    value: int


@dataclass(frozen=True)
class Symbol:
    name: str


@dataclass(frozen=True)
class Unary:
    op: str
    value: object


@dataclass(frozen=True)
class Binary:
    op: str
    left: object
    right: object


@dataclass(frozen=True)
class Call:
    name: str
    arguments: tuple[object, ...]


@dataclass(frozen=True)
class Equality:
    left: object
    right: object


@dataclass(frozen=True)
class IndexTuple:
    index: Symbol
    lower: object
    upper: object


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


TOKEN = re.compile(r"\s*(\*\*|[A-Za-z_][A-Za-z_0-9]*|\d+|[()+,=*/\-])")
FUNCTION_ARITY = {
    "gamma": 1,
    "bilinear": 2,
    "trace": 1,
    "lam": 1,
    "KroneckerDelta": 2,
    "sqrt": 1,
}
SYMBOLS = {"A", "B", "G", "I", "Id4", "IdN", "N", "d", "gamma5", "mu", "nu"}


def lex(text: str) -> list[str]:
    """Lex only; syntax and semantics are enforced by ``Parser``."""
    tokens: list[str] = []
    position = 0
    while position < len(text):
        match = TOKEN.match(text, position)
        if match is None:
            if text[position:].strip() == "":
                break
            raise ParseError("invalid token in frozen expression")
        tokens.append(match.group(1))
        position = match.end()
    return tokens


class Parser:
    def __init__(self, text: str):
        self.tokens = lex(text)
        self.index = 0

    def peek(self) -> str | None:
        return self.tokens[self.index] if self.index < len(self.tokens) else None

    def take(self, value: str | None = None) -> str:
        token = self.peek()
        if token is None or (value is not None and token != value):
            raise ParseError(f"expected {value or 'token'}")
        self.index += 1
        return token

    def parse(self) -> object:
        result = self.equality()
        if self.peek() is not None:
            raise ParseError("trailing frozen expression tokens")
        return result

    def equality(self) -> object:
        left = self.additive()
        if self.peek() == "=":
            self.take("=")
            return Equality(left, self.additive())
        return left

    def additive(self) -> object:
        result = self.multiplicative()
        while self.peek() in {"+", "-"}:
            result = Binary(self.take(), result, self.multiplicative())
        return result

    def multiplicative(self) -> object:
        result = self.power()
        while self.peek() in {"*", "/"}:
            result = Binary(self.take(), result, self.power())
        return result

    def power(self) -> object:
        result = self.unary()
        if self.peek() == "**":
            self.take("**")
            result = Binary("**", result, self.power())
        return result

    def unary(self) -> object:
        if self.peek() in {"+", "-"}:
            return Unary(self.take(), self.unary())
        return self.primary()

    def primary(self) -> object:
        token = self.peek()
        if token is None:
            raise ParseError("unexpected end of frozen expression")
        if token.isdigit():
            return Number(int(self.take()))
        if token == "(":
            self.take("(")
            result = self.equality()
            self.take(")")
            return result
        if re.fullmatch(r"[A-Za-z_][A-Za-z_0-9]*", token):
            name = self.take()
            if self.peek() == "(":
                return self.call(name)
            if name not in SYMBOLS:
                raise ParseError(f"outside frozen vocabulary: {name}")
            return Symbol(name)
        raise ParseError("invalid frozen primary")

    def call(self, name: str) -> object:
        self.take("(")
        if name == "Sum":
            body = self.equality()
            self.take(",")
            index = self.index_tuple()
            self.take(")")
            return Call(name, (body, index))
        arguments: list[object] = []
        if self.peek() != ")":
            arguments.append(self.equality())
            while self.peek() == ",":
                self.take(",")
                arguments.append(self.equality())
        self.take(")")
        if name not in FUNCTION_ARITY or len(arguments) != FUNCTION_ARITY[name]:
            raise ParseError(f"invalid arity for {name}")
        return Call(name, tuple(arguments))

    def index_tuple(self) -> IndexTuple:
        self.take("(")
        index = self.primary()
        if not isinstance(index, Symbol):
            raise ParseError("index tuple requires a symbolic index")
        self.take(",")
        lower = self.equality()
        self.take(",")
        upper = self.equality()
        self.take(")")
        return IndexTuple(index, lower, upper)


def parse(text: str) -> object:
    return Parser(text).parse()


def scalar_ast(value: object) -> sp.Expr:
    """Lower only scalar AST leaves to exact SymPy expressions."""
    if isinstance(value, Number):
        return sp.Integer(value.value)
    if isinstance(value, Symbol) and value.name in {"G", "N"}:
        return sp.Symbol(value.name, nonzero=True)
    if isinstance(value, Unary):
        operand = scalar_ast(value.value)
        return operand if value.op == "+" else -operand
    if isinstance(value, Binary):
        left, right = scalar_ast(value.left), scalar_ast(value.right)
        return {
            "+": left + right,
            "-": left - right,
            "*": left * right,
            "/": left / right,
            "**": left**right,
        }[value.op]
    raise ParseError("non-scalar frozen AST cannot lower to SymPy")


def ast_key(value: object) -> tuple:
    """Structural key with explicit, limited commutative canonicalization."""
    if isinstance(value, Number):
        return ("number", value.value)
    if isinstance(value, Symbol):
        return ("symbol", value.name)
    if isinstance(value, Unary):
        return ("unary", value.op, ast_key(value.value))
    if isinstance(value, Binary):
        left, right = ast_key(value.left), ast_key(value.right)
        if value.op in {"+", "*"}:
            return ("binary", value.op, *sorted((left, right)))
        return ("binary", value.op, left, right)
    if isinstance(value, Call):
        return ("call", value.name, *(ast_key(item) for item in value.arguments))
    if isinstance(value, IndexTuple):
        return (
            "index",
            ast_key(value.index),
            ast_key(value.lower),
            ast_key(value.upper),
        )
    if isinstance(value, Equality):
        return ("equal", ast_key(value.left), ast_key(value.right))
    raise TypeError(value)


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
    if re.fullmatch(r"[SPAVT]+\[A=0\.\.N\*\*2-1\]", compact):
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


def parse_trace_normalization(text: str) -> object:
    return parse(text)


def parse_generator_normalization(text: str) -> object:
    return parse(text)


def parse_grassmann_sign(text: str) -> sp.Integer:
    value = scalar_ast(parse(text))
    if value not in {sp.Integer(-1), sp.Integer(1)}:
        raise ParseError("invalid grassmann crossing sign")
    return value


def expand_basis_expression(
    value: object, domain: Domain, gammas: list[sp.Matrix], gamma5: sp.Matrix
) -> list[sp.Matrix]:
    key = ast_key(value)
    if domain.dimensions == ():
        if key == ast_key(Symbol("Id4")):
            return [sp.eye(4)]
        if key == ast_key(Symbol("gamma5")):
            return [gamma5]
    if len(domain.dimensions) == 1 and domain.dimensions[0][0] == "mu":
        count = int(domain.dimensions[0][1][-1]) + 1
        gamma_mu = ast_key(Call("gamma", (Symbol("mu"),)))
        axial = ast_key(
            Binary(
                "*",
                Binary("*", Symbol("I"), Call("gamma", (Symbol("mu"),))),
                Symbol("gamma5"),
            )
        )
        bare_axial = ast_key(
            Binary("*", Call("gamma", (Symbol("mu"),)), Symbol("gamma5"))
        )
        if key == gamma_mu:
            return list(gammas[:count])
        if key == axial:
            return [sp.I * item * gamma5 for item in gammas[:count]]
        if key == bare_axial:
            return [item * gamma5 for item in gammas[:count]]
    tensor = ast_key(
        Binary(
            "/",
            Binary(
                "*",
                Symbol("I"),
                Binary(
                    "-",
                    Binary(
                        "*",
                        Call("gamma", (Symbol("mu"),)),
                        Call("gamma", (Symbol("nu"),)),
                    ),
                    Binary(
                        "*",
                        Call("gamma", (Symbol("nu"),)),
                        Call("gamma", (Symbol("mu"),)),
                    ),
                ),
            ),
            Number(2),
        )
    )
    if domain.dimensions == (("mu,nu", "0<=mu<nu<=3"),) and key == tensor:
        return [
            sp.I * (gammas[mu] * gammas[nu] - gammas[nu] * gammas[mu]) / 2
            for mu in range(4)
            for nu in range(mu + 1, 4)
        ]
    raise ParseError("basis expression/domain mismatch")
