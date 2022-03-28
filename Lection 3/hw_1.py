# Отсортируйте список случайной длины в зависимости от мода (reverse) по возрастанию или по убыванию
import random

MAX_NUM = 100


def sort(tpl: tuple, reverse: bool = False):
    lst = list(tpl)
    lst_sort = []
    while lst:
        lst_sort.append(lst.pop(lst.index(min(lst))))
    if reverse:
        return lst_sort[::-1]
    return lst_sort


if __name__ == "__main__":
    numbers = tuple(
        random.randint(0, MAX_NUM) for _ in range(random.randint(0, MAX_NUM))
    )
    print(numbers)
    print(sort(numbers, reverse=True))  # change mod here
