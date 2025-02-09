from fastapi import FastAPI
from utils import json_to_dict_list
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, 'students.json')


app = FastAPI()


@app.get('/')
def home_page():
    return {'message': 'Привет мир!'}


@app.get('/student/{student_id}')
def get_student(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student['student_id'] == student_id:
            return [student,]

    return []


@app.get('/student')
def get_student_param(student_id: int | None = None):
    students = json_to_dict_list(path_to_json)
    if student_id is None:
        return []

    for student in students:
        if student['student_id'] == student_id:
            return [student,]

    return []


@app.get('/students')
def get_all_students(course: int | None = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students

    return_list = []
    for student in students:
        if student['course'] == course:
            return_list.append(student)

    return return_list


@app.get('/students/{course}')
def get_all_students_course(course: int,
                            major: str | None = None,
                            enrollment_year: int = None):
    students = json_to_dict_list(path_to_json)
    return_list = []
    for student in students:
        if student['course'] != course:
            continue

        if major and student['major'].lower() != major.lower():
            continue

        if enrollment_year and student['enrollment_year'] != enrollment_year:
            continue

        return_list.append(student)

    return return_list
