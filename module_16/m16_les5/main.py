"""
Шаблонизатор Jinja 2
Цель: научиться взаимодействовать с шаблонами Jinja 2 и использовать их в запросах
"""
from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
import uvicorn

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


# Чтоб не добавлять каждый раз, лениво
user0 = User(id=0, username='user', age=22)
user1 = User(id=1, username='user1', age=23)
user2 = User(id=2, username='user2', age=24)
users.append(user0)
users.append(user1)
users.append(user2)


@app.get('/')
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {"request": request, "users": users})


@app.get('/user/{user_id}')
async def get_all_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {"request": request, "user": users[user_id]})


@app.post('/user/{username}/{age}')
async def add_new_user(username: Annotated[str, Path(min_length=4, max_length=20,
                                                     description='Enter username', example='UrbanUser')],
                       age: Annotated[int, Path(ge=18, le=99,
                                                description='Enter age', example='25')]) -> User:
    current_id = max(user.id for user in users) if users else 0
    new_user = User(id=current_id + 1, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def change_user(user_id: Annotated[int, Path(ge=1, le=999,
                                                   description='Enter user_id', example='1')],
                      username: Annotated[str, Path(min_length=4, max_length=20,
                                                    description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=99,
                                               description='Enter age', example='25')]) -> str:
    find_user = [user for user in users if user.id == user_id]
    if find_user:
        find_user[0].username = username
        find_user[0].age = age
        return f'Пользователь обновлен'
    else:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_users(user_id: Annotated[int, Path(ge=1, le=999,
                                                    description='Enter user_id', example='1')]) -> str:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f'Пользователь удален'
    raise HTTPException(status_code=404, detail="User was not found")


if __name__ == "__main__":
    # http://127.0.0.1:8000/docs
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
