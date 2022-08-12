from typing import Any


class University(type):

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        print(f'==== Estes são os argumentos: {args}')
        return type.__call__(cls, *args, **kwargs)


class Geek(metaclass=University):

    def __init__(self, valor1, valor2) -> None:
        self.valor1 = valor1
        self.valor2 = valor2


obj = Geek(42, 23)

print(obj)
