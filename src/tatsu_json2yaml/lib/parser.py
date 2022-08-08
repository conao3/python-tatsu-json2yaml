from typing import Optional
import tatsu

from . import types


class JsonSemantics:
    def jsonvalue(self, ast):
        match ast:
            case (_, val, _):
                return val
            case _:
                raise ValueError(f'Unexpected jsonvalue: {ast}')

    def jsonobject(self, ast) -> types.JsonObject:
        d = {}
        match ast:
            case ('{', pairs, '}'):
                for pair in pairs:
                    match pair:
                        case (_, key, _, ':', val):
                            d[key.value] = val
                        case _:
                            raise ValueError(f"Unexpected jsonobject->pair: {pair}")
            case _:
                raise ValueError(f"Unexpected jsonobject: {ast}")

        return types.JsonObject(d)

    def jsonarray(self, ast) -> types.JsonArray:
        match ast:
            case ('[', elements, ']'):
                return types.JsonArray(elements)
            case _:
                raise ValueError(f"Unexpected jsonarray: {ast}")

    def jsonstring(self, ast) -> types.JsonString:
        match ast:
            case ('"', val, '"'):
                return types.JsonString(val)
            case _:
                raise ValueError(f"Unexpected jsonstring: {ast}")

    def jsonint(self, ast) -> types.JsonInt:
        return types.JsonInt(int(ast))

    def jsonfloat(self, ast) -> types.JsonFloat:
        return types.JsonFloat(float(ast))

    def jsonsymbol(self, ast) -> types.JsonSymbol:
        match ast:
            case 'true':
                return types.TRUE
            case 'false':
                return types.FALSE
            case 'null':
                return types.NULL
            case _:
                raise ValueError(f"Unexpected jsonsymbol: {ast}")


class Parser:
    def __init__(self):
        with open('./src/tatsu_json2yaml/lib/grammar.ebnf') as f:
            self.grammar = f.read()

        self.model = tatsu.compile(self.grammar, semantics=JsonSemantics())

    def read(self, inpt: str) -> Optional[types.JsonValue]:
        res = self.model.parse(inpt)

        if not res:
            return

        if not isinstance(res, types.JsonValue):
            raise ValueError(f'Unexpected result: {type(res)}, {res}')

        return res
