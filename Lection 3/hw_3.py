# Запишите в словарь по ключам от 1 до 10, список чисел от 0 до 1000, которые делятся на соответствующие ключи
# Пример числа от 1 до 6:
# {
#     1: [1, 2, 3, 4, 5, 6],
#     2: [2, 4, 6],
#     3: [3, 6],
#     ...
# }
from pprint import pprint

KEY_NUMBER = 10
VALUE_NUMBER = 10


def get_dividers_dict():

    return {
        k: [v for v in range(1, VALUE_NUMBER + 1) if v % k == 0]
        for k in range(1, KEY_NUMBER + 1)
    }


if __name__ == "__main__":
    pprint(get_dividers_dict())
