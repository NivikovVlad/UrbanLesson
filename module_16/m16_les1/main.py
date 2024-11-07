"""
Основы Fast Api и маршрутизация
Цель: научиться создавать базовую маршрутизацию для обработки данных в FastAPI
"""
import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def main_page() -> str:
    return 'Главная страница'


# http://127.0.0.1:8000/user/admin
@app.get('/user/admin')
async def admin_panel() -> str:
    return 'Вы вошли как администратор'


# http://127.0.0.1:8000/user/5345
@app.get('/user/{user_id}')
async def user_page(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}>'


# http://127.0.0.1:8000/user?username=Vlad&age=10
@app.get('/user')
async def user_info(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == "__main__":
    # http://127.0.0.1:8000/docs
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)