from typing import Optional


def READ(x: Optional[str]) -> Optional[str]:
    return x


def EVAL(x: Optional[str]) -> Optional[str]:
    return x


def PRINT(x: Optional[str]) -> Optional[str]:
    return x


def rep(inpt: Optional[str]) -> Optional[str]:
    return PRINT(EVAL(READ(inpt)))
