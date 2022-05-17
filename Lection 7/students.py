# Реализуйте класс, который будет вести себя как сервер
# Класс должен принимать запросы GET, POST
# При инициализации должны быть прописаны допустимые пути
# При запросе на не существующий путь, класс должен отдавать ошибку 404
# В обработчиках запросов должны присутствовать блоки try/except и при возникновении ошибки при обработке, необходимо отдавать 500 ошибку
#
# В ответ на запросы должны возвращаться словари со следующей структурой:
# {
#     'status': 'OK',  # 'KO' В случае ошибки
#     'code': 200,  # 404, 500 и тд в зависимости от ошибки
#     'body': None,  # Тело ответа если предполагается запросом в произвольной форме
# }
#
# Обязательные к реализации пути:
# 1. GET '/students' - должен возвращаться список имен (возможно дополнительную информацию)
# взятых из файла (почти база данных) (заполните файл сами)
# 2. POST '/students' - должен дозаписывать в файл имя
# 3. Любой путь, который должен поднимать (raise) 500 ошибку при обращении к нему (опишите как её получить в комментарии)
# 4. Добавьте один путь на ваш выбор
#
# Пример обращения к вашему серверу:
# =============================================
# server = YourServer(routes={'GET': ['/students', '/grades', '/schedule'], 'POST': ['/students']})
# server.get(path='/students')
# >> {'status': OK, 'code': 200, 'body': [{имена взятые из файла}]}
# server.post(path='/students', body={'name': 'Guido van Rossum'}) # Записываем 'Guido van Rossum' в файл
#
# server.get(path='/students')
# >> {'status': OK, 'code': 200, 'body': [{имена взятые из файла + 'Guido van Rossum'}]}
#
# server.get(path='/invalid_path')
# >> {'status': KO, 'code': 404, 'body': None}
# =============================================
# Примеры сверху нужны только для примерного понимания как это должно выглядеть, у вас есть право изменять их по своему выбору
# Но конечная реализация должна соответствовать всем требованиям
import csv


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Students:
    def __init__(self, routes):
        self.routes = routes
        self.routes_get = routes["GET"]
        self.routes_post = routes["POST"]
        self.path_students = "/students"
        self.path_grades = "/grades"

    def get(self, path, param=None):
        data = {}
        try:
            if path in self.routes_get:
                data["status"] = "OK"
                data["code"] = 200
                if path is self.path_students:
                    data["body"] = [
                        student["name"] for student in self.load_students_name()
                    ]
                elif path is self.path_grades:
                    data["body"] = self.student_grade(param)
            else:
                raise Error("wrong path")
        except Error as e:
            if e.args[0] == "wrong path":
                data["status"] = "KO"
                data["code"] = 404
                data["body"] = None
                data["error"] = e.args[0]
            elif e.args[0] == "FileNotFoundError":
                data["status"] = "KO"
                data["code"] = 500
                data["body"] = None
                data["error"] = e.args[0]
        except Exception as e:
            data["status"] = "KO"
            data["code"] = 5001
            data["body"] = None
            data["error"] = e.args[0]
        return data

    # def load_data_student(self, id_student):
    #     students_data = list()
    #     with open('students_inf.csv', 'r', encoding='utf-8', newline='') as f:
    #         reader = csv.DictReader(f,  delimiter = ";")
    #         for row in reader:
    #             students_data.append(row)
    #     return students_data
    def student_grade(self, student_name):
        student_id = [
            student["id_student"]
            for student in self.load_students_name()
            if student["name"] == student_name
        ][0]
        print(student_id)
        student_data = list()
        try:
            with open("students_grades.csv", "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f, delimiter=";")
                for row in reader:
                    if row["id_student"] == student_id:
                        student_data.append(
                            {
                                "grades": row["grades"],
                                "school_subject": row["school_subject"],
                            }
                        )
        except Exception as e:
            if isinstance(e, FileNotFoundError):
                raise Error("FileNotFoundError")
        return student_data

    def load_students_name(self):
        students_name = list()
        try:
            with open("studxents_inf.csv", "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f, delimiter=";")
                for row in reader:
                    students_name.append(
                        {"id_student": row["id_student"], "name": row["name"]}
                    )
        except Exception as e:
            if isinstance(e, FileNotFoundError):
                raise Error("FileNotFoundError")
        return students_name


if __name__ == "__main__":
    server = Students(
        routes={"GET": ["/students", "/grades", "/schedule"], "POST": ["/students"]}
    )
    print(server.get(path="/students"))
    print(server.get(path="/grades", param="Маша"))
