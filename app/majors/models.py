from sqlalchemy import text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true


class Major(Base):

    id: Mapped[int_pk]
    major_name: Mapped[str_uniq]
    major_description: Mapped[str_null_true]
    count_students: Mapped[int] = mapped_column(server_default=text('0'))

    students: Mapped[list['Student']] = relationship(  # noqa # type: ignore
        'Student', back_populates='major')

    def __str__(self):
        name = f'{self.__class__.__name__}'
        name += f'(id={self.id}, major_name={self.major_name!r})'
        return name

    def __repr__(self):
        return str(self)
