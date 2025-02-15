from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, validator, ConfigDict


class SStudent(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    phone_number: str = Field(..., description='Номер телефона в международном формате, начинающийся с "+"') # noqa
    first_name: str = Field(..., min_length=1, max_length=50, description='Имя студента, от 1 до 50 символов') # noqa
    last_name: str = Field(..., min_length=1, max_length=50, description='Фамилия студента, от 1 до 50 символов') # noqa
    date_of_birth: date = Field(..., description='Дата рождения студента в формате ГГГГ-ММ-ДД') # noqa
    email: EmailStr = Field(..., description='Электронная почта студента')
    address: str = Field(..., min_length=10, max_length=200, description='Адрес студента, не более 200 символов') # noqa
    enrollment_year: int = Field(..., ge=2002, description='Год поступления должен быть не меньше 2002') # noqa
    major_id: int = Field(..., ge=1, description='ID специальности студента')
    major: str | None = Field(..., description='Название факультета')
    course: int = Field(..., ge=1, le=5, description='Курс должен быть в диапазоне от 1 до 5') # noqa
    special_notes: Optional[str] = Field(None, max_length=500, description='Дополнительные заметки, не более 500 символов') # noqa

    @validator('phone_number')
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{1,15}$', value):
            error = 'Номер телефона должен начинаться с "+"'
            error += ' и содержать от 1 до 15 цифр'
            raise ValueError(error)
        return value

    @validator('date_of_birth')
    def validate_date_of_birth(cls, value):
        if value and value >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return value


class SStudentAdd(BaseModel):
    phone_number: str = Field(..., description='Номер телефона в международном формате, начинающийся с "+"') # noqa
    first_name: str = Field(..., min_length=1, max_length=50, description='Имя студента, от 1 до 50 символов') # noqa
    last_name: str = Field(..., min_length=1, max_length=50, description='Фамилия студента, от 1 до 50 символов') # noqa
    date_of_birth: date = Field(..., description='Дата рождения студента в формате ГГГГ-ММ-ДД') # noqa
    email: EmailStr = Field(..., description='Электронная почта студента')
    address: str = Field(..., min_length=10, max_length=200, description='Адрес студента, не более 200 символов') # noqa
    enrollment_year: int = Field(..., ge=2002, description='Год поступления должен быть не меньше 2002') # noqa
    major_id: int = Field(..., ge=1, description='ID специальности студента')
    course: int = Field(..., ge=1, le=5, description='Курс должен быть в диапазоне от 1 до 5') # noqa
    special_notes: Optional[str] = Field(None, max_length=500, description='Дополнительные заметки, не более 500 символов') # noqa

    @validator('phone_number')
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{1,15}$', value):
            error = 'Номер телефона должен начинаться с "+"'
            error += ' и содержать от 1 до 15 цифр'
            raise ValueError(error)
        return value

    @validator('date_of_birth')
    def validate_date_of_birth(cls, value):
        if value and value >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return value
