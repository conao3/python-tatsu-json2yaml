from typing import Optional
import tatsu

from . import types


class Parser:
    def __init__(self):
        with open('./src/tatsu_json2yaml/lib/grammar.ebnf') as f:
            self.grammar = f.read()

        self.model = tatsu.compile(self.grammar)

    def read(self, inpt: str) -> Optional[types.JsonValue]:
        return self.model.parse(inpt)
