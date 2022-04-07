# Напишите функцию-обертку для других функций (аргумент - другая функция)
# чтобы итоговый вывод выглядел как "Результат: {результат выполнения обернутой функции}"


def decorator_function(func):
    def wrapper(*args):
        print(f"Результат: {func(*args)}")

    return wrapper


@decorator_function
def sum_numbers(lst):
    return sum(lst)


def print_sum(func, args):
    print(f"Результат: {func(args)}")


def sum_nb(lst):
    return sum(lst)


if __name__ == "__main__":
    lst = list(range(10))
    sum_numbers(lst)
    print_sum(sum_nb, lst)
