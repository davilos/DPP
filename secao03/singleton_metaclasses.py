from typing import Any, Dict
import threading


class MetaSingleton(type):

    __instances: Dict[type, type] = {}
    _loc = threading.Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        with cls._loc:
            if cls not in cls.__instances:
                cls.__instances[cls] = super(MetaSingleton, cls).__call__(
                    *args,
                    **kwargs
                )
        return cls.__instances[cls]


class Logger(metaclass=MetaSingleton):

    def __init__(self, value) -> None:
        self.value = value


def make_singleton(value) -> None:
    sg = Logger(value)
    print(sg.value)


log1 = threading.Thread(target=make_singleton, args=('ola',))
print(f'Log 1: {id(log1)}')

log2 = threading.Thread(target=make_singleton, args=('pessoal',))
print(f'Log 2: {id(log2)}')

log1.start()
log2.start()
