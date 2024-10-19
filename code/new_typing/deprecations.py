# deprecations.py
from warnings import deprecated

@deprecated("Use + instead of calling concatenate()")
def concatenate(first: str, second: str) -> str:
    return first + second

concatenate("three.", "thirteen")
