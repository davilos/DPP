from typing import Any, Dict


class MetaSingleton(type):

    __instances: Dict[type, type] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(
                *args,
                **kwargs
            )
        return cls.__instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


log1 = Logger()
print(f'Log 1: {id(log1)}')

log2 = Logger()
print(f'Log2 : {id(log2)}')
