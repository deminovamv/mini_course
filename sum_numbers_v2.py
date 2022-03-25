"""Разработайте приложение принимающее на вход два числа и
выводящее сумму этих чисел"""


class NumberOperation:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def print_info(self):
        try:
            first_number = float(self.first_number)
            second_number = float(self.second_number)
            print(
                "{} + {} = {:.3f}".format(
                    self.first_number,
                    self.second_number,
                    first_number + second_number
                )
            )
        except ValueError:
            print("Вы ввели слова, мне нужны числа")


if __name__ == "__main__":
    user = NumberOperation(
        input("Введите первое число: "), input("Введите второе число: ")
    )
    user.print_info()
