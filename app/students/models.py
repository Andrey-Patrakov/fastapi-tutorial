from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true
from datetime import date


class Student(Base):

    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    date_of_birth: Mapped[date]
    email: Mapped[str_uniq]
    address: Mapped[str] = mapped_column(Text, nullable=False)
    enrollment_year: Mapped[int]
    course: Mapped[int]
    special_notes: Mapped[str_null_true]
    major_id: Mapped[int] = mapped_column(ForeignKey("majors.id"),
                                          nullable=False)
    major: Mapped["Major"] = relationship("Major", back_populates="students")

    def __str__(self):
        name = f'{self.__class__.__name__}(id={self.id}), '
        name += f'first_name={self.first_name!r}'
        name += f'last_name={self.last_name!r}'
        return name

    def __repr__(self):
        return str(self)


class Major(Base):

    id: Mapped[int_pk]
    major_name: Mapped[str_uniq]
    major_decription: Mapped[str_null_true]
    count_students: Mapped[int] = mapped_column(server_default=text('0'))

    def __str__(self):
        name = f'{self.__class__.__name__}'
        name += f'(id={self.id}, major_name={self.major_name!r})'
        return name

    def __repr__(self):
        return str(self)
