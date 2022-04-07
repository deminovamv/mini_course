# Напишите программу которая сортирует список кортежей людей по их росту
# Функция не должна ничего возвращать, а менять список "in-place"
# from operator import itemgetter

LST = [("Alice", 160), ("John", 180), ("Karen", 163), ("Michael", 182), ("Peter", 172)]


def sorted_by_height():
    global LST
  # LST.sort(key=itemgetter(1), reverse=True)
    LST.sort(key=lambda height: height[1], reverse=True)


if __name__ == "__main__":
    print(LST)
    sorted_by_height()
    print(LST)
