"""
Модели данных Pydantic
Цель: научиться описывать и использовать Pydantic модель
"""
from typing import Annotated, List
import uvicorn
from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> list:
    return users


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
