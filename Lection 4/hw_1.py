# Найдите сумму всех чисел меньше 1000, кратных 3 или 5 с помощью рекурсивной функции
N = 1000


def sum_numbers(n: int):
    if n == 3:
        return n
    elif (n % 3 == 0) or (n % 5 == 0):
        return n + sum_numbers(n - 1)
    else:
        return sum_numbers(n - 1)


if __name__ == "__main__":
    print(sum_numbers(N - 1))
