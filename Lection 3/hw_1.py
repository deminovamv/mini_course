# Отсортируйте список случайной длины в зависимости от мода (reverse) по возрастанию или по убыванию
import random

MAX_NUM = 50


def quick_sort(lst: list):
    if not lst or len(lst) == 1:
        return lst
    separator = lst[0]
    l_lst = [v for i, v in enumerate(lst) if v <= separator and i != 0]
    r_lst = [v for v in lst if v > separator]
    return quick_sort(l_lst) + [separator] + quick_sort(r_lst)


def sort(
    sort_type,
    tpl: tuple,
    reverse: bool = False,
):
    lst = list(tpl)
    if reverse:
        return sort_type(lst)[::-1]
    else:
        return sort_type(lst)


def min_list(lst: list):
    min_el = float("inf")
    index_min = None
    for i, el in enumerate(lst):
        if el < min_el:
            index_min = i
    return index_min


def slow_sort(tpl: tuple, reverse: bool = False):
    lst = list(tpl)
    lst_sort = []
    while lst:
        lst_sort.append(lst.pop(min_list(lst)))
    if reverse:
        return lst_sort[::-1]
    return lst_sort


if __name__ == "__main__":
    numbers = tuple(
        random.randint(0, MAX_NUM) for _ in range(random.randint(0, MAX_NUM))
    )
    print(numbers)
    sort_type = quick_sort
    print(sort(sort_type, numbers, reverse=False))  # change mod here
