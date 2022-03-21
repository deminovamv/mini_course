"""Разработайте приложение принимающее на вход два числа и
выводящее сумму этих чисел"""
import re


class NumberOperation:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def print_info(self):
        while True:
            match_first = re.match(r"^[\d]{1,}$", self.first_number)
            match_second = re.match(r"^[\d]{1,}$", self.second_number)
            if match_first and match_second:
                print(
                    "{} + {} = {}".format(
                        self.first_number,
                        self.second_number,
                        int(self.first_number) + int(self.second_number),
                    )
                )
                break
            elif not match_first and match_second:
                self.first_number = input("Пожалуйста, введите первое число цифрой: ")
            elif match_first and not match_second:
                self.second_number = input("Пожалуйста, введите второе число цифрой: ")

            else:
                self.first_number = input("Пожалуйста, введите первое число цифрой: ")
                self.second_number = input("Пожалуйста, введите второе число цифрой: ")


if __name__ == "__main__":
    user = NumberOperation(
        input("Введите первое число: "), input("Введите второе число: ")
    )
    user.print_info()
