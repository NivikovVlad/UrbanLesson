"""
Валидация данных
Цель: научится писать необходимую валидацию для вводимых данных при помощи классов Path и Annotated
"""
from typing import Annotated
import uvicorn
from fastapi import FastAPI, Path


app = FastAPI()


@app.get('/')
async def main_page() -> str:
    return 'Главная страница'


# http://127.0.0.1:8000/user/admin
@app.get('/user/admin')
async def admin_panel() -> str:
    return 'Вы вошли как администратор'


# http://127.0.0.1:8000/user/30
@app.get('/user/{user_id}')
async def user_page(user_id: Annotated[int, Path(ge=1, le=100,
                                                 description='Enter User ID', example='25')]) -> str:
    return f'Вы вошли как пользователь № {user_id}>'


# http://127.0.0.1:8000/user/Vlad/10
@app.get('/user/{username}/{age}')
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20,
                                                  description='Enter username', example='UrbanUser')],
                    age: Annotated[int, Path(ge=18, le=120,
                                             description='Enter age', example='25')]) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == "__main__":
    # http://127.0.0.1:8000/docs
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)