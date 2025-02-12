from fastapi import FastAPI


# uvicorn app.main:app --reload
app = FastAPI()


@app.get('/')
def home_page():
    return {'message': 'Привет мир!'}
