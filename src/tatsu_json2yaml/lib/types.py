import tatsu.objectmodel


class JsonValue(tatsu.objectmodel.Node):
    def __init__(self, value):
        self.value = value


class JsonObject(JsonValue):
    pass


class JsonArray(JsonValue):
    pass


class JsonString(JsonValue):
    pass


class JsonNumber(JsonValue):
    pass


class JsonInt(JsonNumber):
    pass


class JsonFloat(JsonNumber):
    pass


class JsonSymbol(JsonValue):
    pass


FALSE = JsonSymbol('false')
TRUE = JsonSymbol('true')
NULL = JsonSymbol('null')
