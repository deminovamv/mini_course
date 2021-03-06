# Напишите класс Building
# Необходимые атрибуты класса: дверь (состояние open/closed) (Может быть отдельным объектом), адрес, площадь
# Класс должен иметь методы open_door, close_door
# * Напишите два класса-наследника Building.
# В первом классе добавьте атрибут со списком окон и возможностью их закрывать/открывать
# Второй придумайте сами и добавьте к нему два любых метода
# **
# 1. Добавьте в классы возможность вывода через print({Building})) в формате
# "{Тип строения} по адресу {адрес}. Дверь {открыта/закрыта}"
# 2. Добавьте логику сложения двух строений. (Достаточно если будет реализовано только для двух строений одного и того же типа, для двух разных типов по желанию)
# Итогом сложения должен быть объект по адресу строения с наибольшей площадью из слагаемых, с площадью равной суммарной площади двух строений
# И дверь должна быть открыта если хотя бы одно из исходных строений было с открытой дверью
import collections


class Building:
    def __init__(self, door: bool, address: str, area: float):
        self.door = door
        self.address = address
        self.area = area

    def open_door(self):
        if not self.door:
            self.door = True

    def close_door(self):
        if self.door:
            self.door = False

    def __str__(self):
        return f"У строения по адресу {self.address}. Дверь {'открыта' if self.door else 'закрыта'}. Площадь равна {self.area}"

    def __add__(self, other):
        if self.area >= other.area:
            address = self.address
        else:
            address = other.address
        if self.door or other.door:
            door = True
        else:
            door = False
        area = self.area + other.area

        return Building(door, address, area)


class Apartment(Building):
    def __init__(self, door: bool, address: str, area: float, list_window: list):
        self.list_window = list_window
        super().__init__(door, address, area)

    def index_check(func):
        def wrapper(self, index):
            if 0 <= index < len(self.list_window):
                func(self, index)
            else:
                print("Нет окна с таком номером")

        return wrapper

    @index_check
    def open(self, index):
        self.list_window[index] = True

    @index_check
    def close(self, index):
        self.list_window[index] = False

    def __str__(self):
        return f"У квартиры по адресу {self.address}. Дверь {'открыта' if self.door else 'закрыта'}. Площадь равна {self.area}"

    def open_window_check(self):
        window_check = collections.Counter(self.list_window)
        if not window_check.get(True):
            print("В квартире все окна закрыты")
        elif not window_check.get(False):
            print("В квартире все окна открыты")
        else:
            print("В квартире есть открытые окна")


class СountryHouse(Building):
    def __init__(self, door: bool, address: str, area: float, fence: bool):
        self.fence = fence
        super().__init__(door, address, area)

    def add_fence(self):
        if self.fence:
            print(f"На даче по адресу {self.address} уже есть забор")
        else:
            self.fence = True

    def check_fence(self):
        print(
            f"На даче по адресу {self.address} { 'есть забор' if self.fence else 'забора нет'}"
        )

    def __str__(self):
        return f"На даче по адресу {self.address}. Дверь {'открыта' if self.door else 'закрыта'}. Площадь равна {self.area}"


if __name__ == "__main__":

    building_2 = Apartment(False, "УЛИЦА 1", 23, [True for _ in range(5)])
    building_2.open_window_check()
    building_2.close(2)
    print(building_2.list_window)
    building_2.close(1)
    print(building_2.list_window)
    print(building_2)
    building_2.open_door()
    print(building_2)
    building_2.open_window_check()
    building_2.close_door()

    building_3 = СountryHouse(False, "УЛИЦА 2", 50, False)
    print(building_3)
    building_3.check_fence()
    building_3.add_fence()
    building_3.check_fence()
    building_3.add_fence()
    building_4 = building_2 + building_3
    print(building_4)
    print(building_2 + building_3)
