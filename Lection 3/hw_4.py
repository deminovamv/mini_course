# Реализуйте хеш-таблицу на основе списка.
# Хешировать будем только целые числа.
# Хеш-функция (_hash()) должна возвращать индекс элемента в списке. Пример ниже
# Выбор способа хеширования оставляю за вами, можно придумать свой, можно подглядеть в интернете
# Необходимо реализовать методы add, get, delete и print, позволяющий вывести список в удобном виде
# На первом этапе можно игнорировать коллизии и увеличение storage, необходимо подобрать функцию
# и размер storage (в идеале придумать способо разрещения таких случаев)
# такие, чтобы полученные индексы не выходили за размер storage
# Список не должен менять размер свой размер в процессе использования кроме **

# * Реализуйте разрешение коллизий любым методом на ваш выбор
# ** Реализуйте автоматическое увеличение bucket-ов при заполнении половины существующих

# Пример:
# При инициализации таблицы создаем пустой storage из десяти бакетов:
# [None, None, None, None, None, None, None, None, None, None]
# Пусть функция хеширования выглядит как:
#
# def hash(self, value):
#     return value // 5 + 3
#
# Тогда при попытке положить элемент 30 в таблицу мы положим его в ячейку с индексом 30 // 5 + 3 = 9
# Наш storage будет выглядеть теперь так:
# [None, None, None, None, None, None, None, None, None, 30]
#
# P.S. Во всех заранее созданных методах класса обращаться к storage можно через self.storage
import random
from pprint import pprint
import typing as t

INITIAL_SIZE = 10 ** 4
MULTIPLIER = 3


class HashTable:
    def __init__(self):
        # Create buckets for our Table with None in each bucket
        self.storage = [None] * INITIAL_SIZE

    def add(self, value) -> t.Optional[int]:
        # Add value to storage, return index/hash on success, None on failure
        index = self._hash(value)
        if not self.storage[index]:
            self.storage[index] = value
            return index
        else:
            if isinstance(self.storage[index], list):
                self.storage[index].append(value)
            else:
                self.storage[index] = [self.storage[index]]
                self.storage[index].append(value)
            return index

    def find(self, value) -> int:
        # Find value in storage and return its index
        index = self._hash(value)
        if not self.storage[index]:
            return None
        if isinstance(self.storage[index], list):
            for i, el in enumerate(self.storage[index]):
                if el == value:
                    return index, i
        elif self.storage[index] == value:
            return index
        else:
            return None

    def delete(self, value) -> bool:
        # Delete value from storage, return True on success, return False on failure
        index = self.find(value)
        if type(index) is tuple:
            self.storage[index[0]].pop(index[1])
            if not self.storage[index[0]]:
                self.storage[index] = None
            return True
        elif index:
            self.storage[index] = None
            return True
        else:
            return False

    def _hash(self, value) -> int:
        # Based on value return index of element
        # value = (value ** 2 // 3)

        hash_value = value % INITIAL_SIZE
        return hash_value

    def print(self):
        pprint({k: v for k, v in enumerate(self.storage) if v})

    def factor_downloads(self):
        print(len([v for v in self.storage if v]) / len(self.storage))


if __name__ == "__main__":
    hash_table = HashTable()
    for _ in range(INITIAL_SIZE // MULTIPLIER):
        hash_table.add(random.choice(range(INITIAL_SIZE * MULTIPLIER)))
    hash_table.print()
    hash_table.factor_downloads()
    # print(hash_table.delete(11))
    # print(hash_table.delete(12))
    # print(hash_table.delete(13))
    # print(hash_table.delete(14))
    # print(hash_table.delete(15))
    # print(hash_table.delete(16))
    # print(hash_table.delete(17))
    # hash_table.print()
