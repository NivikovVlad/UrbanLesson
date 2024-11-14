"""
CRUD Запросы: Get, Post, Put Delete
Цель: выработать навык работы с CRUD запросами
"""
from typing import Annotated
import uvicorn
from fastapi import FastAPI, Path


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_new_user(username: str, age: int) -> str:
    current_id = int(max(users, key=int))
    users[current_id + 1] = f'Имя: {username}, возраст: {age}'
    return f'User {current_id + 1} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def replace_user(user_id: int, username: str, age: int) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_users(user_id: int) -> str:
    users.pop(str(user_id))
    return f'User {user_id} is deleted'


if __name__ == "__main__":
    # http://127.0.0.1:8000/docs
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)