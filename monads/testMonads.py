from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")

class Maybe(ABC, Generic[T]):
    """The abstract base class for the Maybe Monad."""
    
    @abstractmethod
    def bind(self, func: Callable[[T], Maybe[U]]) -> Maybe[U]:
        pass

    @staticmethod
    def unit(value: T) -> Maybe[T]:
        """Wraps a value into the appropriate Maybe context."""
        return Nothing() if value is None else Just(value)


class Just(Maybe[T]):
    """Represents a successful state containing a value."""
    def __init__(self, value: T) -> None:
        self.value = value

    def bind(self, func: Callable[[T], Maybe[U]]) -> Maybe[U]:
        # Unwrap, apply the function, and return the new monad
        return func(self.value)

    def __repr__(self) -> str:
        return f"Just({self.value})"


class Nothing(Maybe[Any]):
    """Represents a failure or empty state."""
    def bind(self, func: Callable[[Any], Maybe[U]]) -> Maybe[U]:
        # Short-circuit: skip the function entirely and propagate Nothing
        return self

    def __repr__(self) -> str:
        return "Nothing"

def main():
    add_one = lambda x: Maybe.unit(x + 1)
    multiply_by_two = lambda x: Maybe.unit(x * 2)

    # To handle multi-argument functions like division, use a closure/currying:
    safe_divide_by = lambda y: lambda x: Nothing() if y == 0 else Maybe.unit(x / y)

    # --- Scenario 1: Successful Chain ---
    initial = Maybe.unit(5)
    result = initial.bind(add_one).bind(multiply_by_two)
    print(result)  # Output: Just(12)

    # --- Scenario 2: Error Short-Circuiting ---
    # We pass the value into the closure to get our single-argument function
    divide_by_zero = safe_divide_by(0) 
    
    failed_result = initial.bind(divide_by_zero).bind(add_one)
    print(failed_result)  # Output: Nothing (add_one never executed!)

if __name__ == "__main__":
    main()