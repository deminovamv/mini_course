""" Реализовать программу, которая спрашивает у пользователя: имя,
фамилию, год рождения. После ввода всех данных программа должна
выводить строку с данными"""
import re


class UserInformation:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_info(self):
        while True:
            match = re.match(r"^[\d]{1,}$", self.age)
            if match:
                print(
                    "Hello {} {} your age is {} year".format(
                        self.name, self.surname, self.age
                    )
                )
                break
            else:
                self.age = input("Пожалуста, введите свой возраст цифрами: ")


if __name__ == "__main__":
    user = UserInformation(
        input("Введите своё имя: "),
        input("Введите свою фамилию: "),
        input("Введите свой возраст: "),
    )
    user.print_info()
    