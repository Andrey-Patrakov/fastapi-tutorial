import httpx
import asyncio


async def add_major(major_name: str, major_description: str):
    url = 'http://127.0.0.1:8000/majors/add/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'major_name': major_name,
        'major_description': major_description,
        'cout_students': 0
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        return response.json()


majors = [
    ('Математика', 'Факультет математики'),
    ('Информатика', 'Факультет информатики'),
    ('Русский язык', 'Факультет русского языка'),
    ('Экономика', 'Факультет экономики'),
    ('Психология', 'Факультет психологии'),
    ('Химия', 'Факультет химии'),
    ('История', 'Факультет истории'),
]

for name, description in majors:
    response = asyncio.run(add_major(major_name=name,
                                     major_description=description))
    print(response)
