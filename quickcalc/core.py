from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Union

Number = Union[int, float]


class DivisionByZeroError(ValueError):
    """Raised when attempting to divide by zero."""


def add(a: Number, b: Number) -> float:
    return float(a) + float(b)


def subtract(a: Number, b: Number) -> float:
    return float(a) - float(b)


def multiply(a: Number, b: Number) -> float:
    return float(a) * float(b)


def divide(a: Number, b: Number) -> float:
    b = float(b)
    if b == 0.0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return float(a) / b


@dataclass
class CalcState:
    display: str = "0"
    _current_value: Optional[float] = None
    _pending_op: Optional[str] = None
    _rhs_value: Optional[float] = None

    def clear(self) -> None:
        self.display = "0"
        self._current_value = None
        self._pending_op = None
        self._rhs_value = None

    def input_number(self, token: str) -> None:
        value = float(token)
        self.display = _format_number(value)
        if self._current_value is None:
            self._current_value = value
        else:
            self._rhs_value = value

    def input_operator(self, op: str) -> None:
        if op not in {"+", "-", "*", "/"}:
            raise ValueError(f"Unknown operator: {op}")

        # Chain operations if we already have current + rhs + pending op
        if self._pending_op and self._current_value is not None and self._rhs_value is not None:
            self._apply_pending()

        self._pending_op = op

    def equals(self) -> None:
        if not self._pending_op:
            return

        if self._current_value is None:
            self._current_value = 0.0

        # If RHS missing, use current value (common calculator behavior)
        if self._rhs_value is None:
            self._rhs_value = self._current_value

        self._apply_pending()
        self._pending_op = None
        self._rhs_value = None

    def _apply_pending(self) -> None:
        a = self._current_value
        b = self._rhs_value
        if a is None or b is None or self._pending_op is None:
            return

        if self._pending_op == "+":
            res = add(a, b)
        elif self._pending_op == "-":
            res = subtract(a, b)
        elif self._pending_op == "*":
            res = multiply(a, b)
        else:
            res = divide(a, b)

        self._current_value = res
        self.display = _format_number(res)


def evaluate_sequence(tokens: List[str]) -> str:
    state = CalcState()

    for tok in tokens:
        tok = tok.strip()
        if not tok:
            continue

        if tok.upper() == "C":
            state.clear()
            continue

        if tok == "=":
            try:
                state.equals()
            except DivisionByZeroError:
                state.display = "Error"
                state.clear()
                state.display = "Error"
            continue

        if tok in {"+", "-", "*", "/"}:
            state.input_operator(tok)
            continue

        # number
        state.input_number(tok)

    return state.display


def _format_number(x: float) -> str:
    if x.is_integer():
        return str(int(x))
    return str(x)