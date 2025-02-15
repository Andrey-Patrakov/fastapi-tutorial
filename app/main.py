from fastapi import FastAPI
from app.students.router import router as router_students
from app.majors.router import router as router_majors

# uvicorn app.main:app --reload
app = FastAPI()


@app.get('/')
def home_page():
    return {'message': 'Привет мир!'}


app.include_router(router_students)
app.include_router(router_majors)
