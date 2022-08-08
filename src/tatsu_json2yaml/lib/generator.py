import tatsu.codegen
import tatsu.util

from . import types


indent = lambda x: tatsu.util.indent(x, multiplier=2)


class Json2YamlGenerator(tatsu.codegen.CodeGenerator):
    def _find_renderer_class(self, node):
        for cls in node.__class__.__mro__:
            if fn := getattr(self, cls.__name__, None):
                return fn

    class JsonObject(tatsu.codegen.ModelRenderer):
        def render_fields(self, fields):
            def rend_v(v):
                if isinstance(v, (types.JsonObject, types.JsonArray)):
                    return f'\n{indent(self.rend(v))}'
                else:
                    return self.rend(v)

            form = '\n'.join([f'{self.rend(k)}: {rend_v(v)}' for k, v in self.value.items()])
            fields.update(form=form)

        template = '''\
        {form}'''

    class JsonArray(tatsu.codegen.ModelRenderer):
        def render_fields(self, fields):
            form = '\n'.join([self.rend(v) for v in self.value])
            fields.update(form=indent(form)[2:])

        template = '''\
        - {form}'''


    class JsonString(tatsu.codegen.ModelRenderer):
        template = '''\
        "{value}"'''

    class JsonNumber(tatsu.codegen.ModelRenderer):
        template = '''\
        {value}'''

    class JsonSymbol(tatsu.codegen.ModelRenderer):
        template = '''\
        {value}'''
