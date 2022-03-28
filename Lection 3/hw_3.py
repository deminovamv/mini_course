# Запишите в словарь по ключам от 1 до 10, список чисел от 0 до 1000, которые делятся на соответствующие ключи
# Пример числа от 1 до 6:
# {
#     1: [1, 2, 3, 4, 5, 6],
#     2: [2, 4, 6],
#     3: [3, 6],
#     ...
# }
from pprint import pprint


def get_dividers_dict():
    key_number = 10
    value_number = 10
    return {
        k: [v for v in range(1, value_number + 1) if v % k == 0]
        for k in range(1, key_number + 1)
    }


if __name__ == "__main__":
    pprint(get_dividers_dict())
