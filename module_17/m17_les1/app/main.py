import uvicorn
from fastapi import FastAPI
from routers import task, user


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
app.include_router(task.router)
app.include_router(user.router)


@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


if __name__ == "__main__":
    # http://127.0.0.1:8000/docs
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
