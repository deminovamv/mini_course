import csv
from error import *


class Students:
    def __init__(self, routes):
        self.routes = routes
        self.routes_get = routes["GET"]
        self.routes_post = routes["POST"]
        self.path_students = routes["GET"][0]
        self.path_grades = routes["GET"][1]
        self.path_students_add = routes["POST"][0]
        self.path_student_grades_add = routes["POST"][1]

    def answer(func):
        def wrapper(self, path, param=None, body=None):
            data = {}
            data["body"] = None
            data["code"] = None
            try:
                if path in self.routes_get and not body:
                    data["body"] = func(self, path, param)
                elif path in self.routes_post and body:
                    data["body"] = func(self, path, body)
                else:
                    raise WrongPath(path)
            except (WrongPath, NameNotFound, StudentError) as e:
                data["error"] = e.text_error()
            except FileNotFoundError as e:
                data["code"] = 500  # 500 , когда файл не найден
                data["error"] = e
            except Exception as e:
                data["code"] = 500
                data["error"] = e
            finally:
                if data["body"]:
                    data["status"] = "OK"
                    data["code"] = 200
                else:
                    data["status"] = "KO"
                    data["body"] = None
                    if data["code"] != 500:
                        data["code"] = 404
            return data

        return wrapper

    @answer
    def get(self, path, param=None):
        if path == self.path_students:
            body = self.load_students_name()
        else:
            body = self.student_grades(param)
        return body

    @answer
    def post(self, path, body):
        if path == self.path_students_add:
            data = self.student_add(body)
        else:
            data = self.student_grades_add(body)
        return data

    def student_add(self, body):
        """
        Функция проверяет есть ли такой студент в файле, если нет, то добавлет его
        """

        try:
            if not body["name"] in self.load_students_name():
                with open("students_inf.csv", "r+", encoding="utf-8", newline="") as f:
                    f.seek(0, 2)  # перемещение курсора в конец файла
                    student_writer = csv.writer(f, delimiter=";")
                    student_writer.writerow([body["name"]])
            else:
                raise StudentError(f"{body['name']} is in the file")
        except FileNotFoundError as e:
            raise e
        except Exception as e:
            raise e
        return body["name"]

    def load_students_name(self):
        """
        Функция возвращает список всех студентов
        """
        students_name = list()
        try:
            with open("students_inf.csv", "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f, delimiter=";")
                for row in reader:
                    students_name.append(row["name"])
        except FileNotFoundError as e:
            raise e
        except Exception as e:
            raise e
        return students_name

    def student_grades(self, student_name):
        """
        Выводит все оценки, которые есть у студента, если они есть
        """
        student_data = list()
        try:
            if student_name in self.load_students_name():
                with open(
                    "students_grades.csv", "r", encoding="utf-8", newline=""
                ) as f:
                    reader = csv.DictReader(f, delimiter=";")
                    for row in reader:
                        if row["student_name"] == student_name:
                            student_data.append(
                                {
                                    "grades": row["grades"],
                                    "school_subject": row["school_subject"],
                                }
                            )
                    if not student_data:
                        raise StudentError("student has no grades")
            else:
                raise NameNotFound(student_name)
        except FileNotFoundError as e:
            raise e
        except Exception as e:
            raise e
        return student_data

    def student_grades_add(self, body):
        """
        Добавляет оценки в файл, если таких оценок ещё не было
        """
        try:
            grades = {
                "grades": body["grades"],
                "school_subject": body["school_subject"],
            }
            if grades in self.student_grades(body["name"]):
                raise StudentError("such assessments already exist")
            else:
                with open(
                    "students_grades.csv", "r+", encoding="utf-8", newline=""
                ) as f:
                    f.seek(0, 2)
                    student_writer = csv.writer(f, delimiter=";")
                    student_writer.writerow(body.values())
        except FileNotFoundError as e:
            raise e
        except Exception as e:
            raise e
        return body
