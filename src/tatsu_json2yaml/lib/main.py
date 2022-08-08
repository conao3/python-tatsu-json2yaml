from typing import Optional

from . import parser
from . import types

parser_ = parser.Parser()


def READ(x: Optional[str]) -> Optional[types.JsonValue]:
    if x:
        return parser_.read(x)


def EVAL(x: Optional[types.JsonValue]) -> Optional[types.JsonValue]:
    return x


def PRINT(x: Optional[types.JsonValue]) -> Optional[str]:
    if x:
        return str(x)


def rep(inpt: Optional[str]) -> Optional[str]:
    return PRINT(EVAL(READ(inpt)))
