# Выведите все простые числа для заданного интервала
# Гарантируется, что start и end типа int. Вводятся в одну строку через пробел


def number_check(number: int):
    for k in range(2, int(number / 2) + 1):
        if number % k == 0:
            return False
    return True


def get_prime_nums(start: int, end: int):
    if start >= end:
        return print("некорректные значения интервала")
    elif start < 1:
        start = 2
    for i in range(start, end):
        if number_check(i):
            print(i)


if __name__ == "__main__":
    start, end = map(int, input().split())
    get_prime_nums(
        start=start,
        end=end,
    )
