import requests


def get_all_students():
    url = 'http://127.0.0.1:8000/students'
    respose = requests.get(url)
    return respose.json()


def get_all_students_with_param_requests(course: int):
    url = 'http://127.0.0.1:8000/students'
    respose = requests.get(url, params={'course': course})
    return respose.json()


def get_all_students_with_param_path(course: int):
    url = f'http://127.0.0.1:8000/students/{course}'
    respose = requests.get(url)
    return respose.json()


students = get_all_students()
for student in students:
    print(student)


print('='*30)
students = get_all_students_with_param_requests(course=2)
for student in students:
    print(student)


print('='*30)
students = get_all_students_with_param_path(course=2)
for student in students:
    print(student)
