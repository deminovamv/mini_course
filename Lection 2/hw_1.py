"""Выведите последовательность чисел от 112..133 в обратном порядке
различными типами цикла (while и for)
"""


def sequence_output(sequence: list):
    for i in range(len(sequence) - 1, -1, -1):
        print(sequence[i], end=" ")
    print()
    i = len(sequence) - 1
    while i >= 0:
        print(sequence[i], end=" ")
        i -= 1
    print()
    print(" ".join([str(i) for i in sequence[::-1]]))


if __name__ == "__main__":
    sequence = [i for i in range(112, 134)]
    sequence_output(sequence)
