# Найдите сумму всех чисел меньше 1000, кратных 3 или 5 с помощью функции генератора


def gen_func(n: int):
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            yield i


if __name__ == "__main__":
    lst = gen_func(1000)
    print(sum(lst))
