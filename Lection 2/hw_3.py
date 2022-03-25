# На входе последовательность из десяти чисел, выведите максимально возможную сумму трех из этих чисел
import random

MAX_NUM = 100000


def get_max_sum_of_three(numbers: tuple):
    max_1 = max(numbers[0], max(numbers[1], numbers[2]))
    max_3 = min(numbers[0], min(numbers[1], numbers[2]))
    max_2 = sum(numbers[:3]) - max_3 - max_1
    # return print(max_1,max_2,max_3)
    for index in range(3, len(numbers)):
        if numbers[index] >= max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = numbers[index]
        elif numbers[index] >= max_2:
            max_3 = max_2
            max_2 = numbers[index]
        elif numbers[index] >= max_3:
            max_3 = numbers[index]
    return print(max_1 + max_2 + max_3)


def get_max_sum_of_three_check(numbers: tuple):
    numbers_list = list(numbers)
    return print(sum(sorted(numbers)[len(numbers_list) - 3 :]))


if __name__ == "__main__":
    numbers = tuple(random.randint(0, MAX_NUM) for _ in range(10))
    print(numbers)
    get_max_sum_of_three(numbers)
    get_max_sum_of_three_check(numbers)
