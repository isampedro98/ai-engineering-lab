# AI Engineering Lab

Personal repository for small experiments in programming, agents, automation, and applied AI concepts.

The point is not to start with a large product, but with concrete, understandable pieces that can be discarded if needed. This repository documents that process from zero.

## First experiment

`monads/testMonads.py` implements a minimal version of the `Maybe` monad in Python:

- `Just(value)` represents a valid value.
- `Nothing()` represents the absence of a value or an error.
- `bind(...)` chains operations without having to check for errors at every step.

The example shows two cases:

1. A successful transformation chain.
2. An early short-circuit when an invalid operation appears.

## Repository goal

The plan is to keep adding short experiments that help:

- practice functional programming concepts and modeling
- test ideas related to AI and automation
- keep a record of learning, even when the result is simple

## Note

The first program is intentionally small. That does not reduce its value: it sets the tone for the repository and provides a clear base to iterate on.
