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
import students

if __name__ == "__main__":
    server = students.Students(
        routes={"GET": ["/students", "/grades"], "POST": ["/students", "/grades"]}
    )
    print(server.get(path="/students"))
    print(server.get(path="/grades", param="Даша"))
    print(server.post(path="/students", body={"name": "Виктор"}))
    print(server.get(path="/grades", param="Викто1111р"))
    print(
        server.post(
            path="/grades",
            body={
                "name": "Маша",
                "grades": "2,5,5,3,3,4,5",
                "school_subject": "история",
            },
        )
    )
    # ответы:
    # {'body': ['Маша', 'Даша', 'Катя', 'Саша', 'Guido van Rossum', 'Виктор'], 'code': 200, 'status': 'OK'}
    # {'body': [{'grades': '2,5,5,3,4,5', 'school_subject': 'литература'},
    #           {'grades': '2,5,5,3,4,5', 'school_subject': 'история'},
    #           {'grades': '2,5,5,5,4,5', 'school_subject': 'история'},
    #           {'grades': '2,5,5,3,3,4,5', 'school_subject': 'история'}], 'code': 200, 'status': 'OK'}
    # {'body': None, 'code': 404, 'error': 'Виктор is in the file', 'status': 'KO'}
    # {'body': None, 'code': 404, 'error': 'NameNotFound, Викто1111р ', 'status': 'KO'}
    # {'body': None, 'code': 404, 'error': 'such assessments already exist', 'status': 'KO'}
