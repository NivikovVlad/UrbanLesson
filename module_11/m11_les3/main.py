"""
Интроспекция
Закрепить знания об интроспекции в Python.
Создать персональную функции для подробной интроспекции объекта
"""
import sys
from pprint import pprint


def introspection_info(obj):
    result = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': obj.__module__ if hasattr(obj, '__module__') else introspection_info.__module__,
        'callable': callable(obj)
    }
    if isinstance(obj, int):
        result['bit_length'] = obj.bit_length()

    return result


if __name__ == '__main__':
    number_info = introspection_info(42)
    pprint(number_info)



