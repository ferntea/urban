# module_16_4 Модели данных Pydantic

'''
Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:

    id - номер пользователя (int)
    username - имя пользователя (str)
    age - возраст пользователя (int)


Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:

    Добавляет в список users объект User.
    id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
    Все остальные параметры объекта User - переданные в функцию username и age соответственно.
    В конце возвращает созданного пользователя.

put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:

    Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
    В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.

delete запрос по маршруту '/user/{user_id}', теперь:

    Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
    В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.

Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
1. GET '/users'
[]
2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
3. POST '/user/{username}/{age}' # username - UrbanTest, age - 36
4. POST '/user/{username}/{age}' # username - Admin, age - 42
5. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
6. DELETE '/user/{user_id}' # user_id - 2
7. GET '/users'
8. DELETE '/user/{user_id}' # user_id - 2
'''

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# User model
class User(BaseModel):
    id: int
    username: str
    age: int

# Initialisation
users: List[User] = []

@app.get("/")
async def read_root():
    return {"message": "Главная страница"}

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
    username: str,
    age: int
):
    # Determine new user ID
    new_user_id = 1 if not users else users[-1].id + 1
    new_user = User(id=new_user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
    user_id: int,
    username: str,
    age: int
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
    user_id: int
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
