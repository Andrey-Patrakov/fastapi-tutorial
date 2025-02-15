from typing import List
from fastapi import APIRouter, Depends

from app.students.dao import StudentDAO
from app.students.schemas import SStudent, SStudentAdd
from app.students.rb import RBStudent

router = APIRouter(prefix='/students', tags=['Работа со студентами'])


@router.get('/', summary='Получить всех студентов')
async def get_all_students(
        request_body: RBStudent = Depends()) -> List[SStudent]:

    return await StudentDAO.find_all(**request_body.to_dict())


@router.get('/by_filter', summary='Получить одного студена по фильтру')
async def get_student_by_filter(
        request_body: RBStudent = Depends()) -> SStudent | dict:

    result = await StudentDAO.find_one_or_none(**request_body.to_dict())
    if result is None:
        return {'message': 'Студент с указанными параметрами не найден!'}

    return result


@router.get('/{id}', summary='Получить одного студента по id')
async def get_student_by_id(student_id: int) -> SStudent | dict:
    result = await StudentDAO.find_full_data(student_id)
    if result is None:
        return {'message': f'Студент с ID {student_id} не найден!'}

    return result


@router.post('/add/')
async def add_student(student: SStudentAdd) -> dict:
    check = await StudentDAO.add_student(student.model_dump())
    if check:
        return {'message': 'Студент успешно добавлен!',
                'student': student}

    return {'message': 'Ошибка при добавлении студента!'}


@router.delete('del/{student_id}')
async def del_student_by_id(student_id: int) -> dict:
    check = await StudentDAO.delete_student_by_id(student_id=student_id)
    if check:
        return {'message': f'Студент с ID {student_id} удален!'}

    return {'message': 'Ошибка при удалении студента!'}
