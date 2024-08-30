# module_16_2 Валидация данных

'''
Задача "Аннотация и валидация":
Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:
'/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id, для которого необходимо
написать следующую валидацию:

    Должно быть целым числом
    Ограничено по значению: больше или равно 1 и меньше либо равно 100.
    Описание - 'Enter User ID'
    Пример - '1' (можете подставить свой пример не противоречащий валидации)

'/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту, принимает аргументы username
и age, для которых необходимо написать следующую валидацию:

    username - строка, age - целое число.
    username ограничение по длине: больше или равно 5 и меньше либо равно 20.
    age ограничение по значению: больше или равно 18 и меньше либо равно 120.
    Описания для username и age - 'Enter username' и 'Enter age' соответственно.
    Примеры для username и age - 'UrbanUser' и '24' соответственно. (можете подставить свои примеры не противоречащие
    валидации).


Пример результата выполнения программы:
Ошибки валидации для маршрутов '/user/{user_id}' и '/user/{username}/{age}' :
Как должен выглядеть Swagger:

Примечания:

    Если у вас не отображаются параметры Path, проверьте, сделали вы присвоение данных или подсказку типа.
    Верно: username: Annotated[...]. Не верно: username = Annotated[...]
'''

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user(
    user_id: Annotated[int, Path(
        title="Enter User ID",
        ge=1,  # больше или равно 1
        le=100  # меньше или равно 100
    )]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[str, Path(
        title="Enter username",
        min_length=5,  # больше или равно 5
        max_length=20  # меньше или равно 20
    )],
    age: Annotated[int, Path(
        title="Enter age",
        ge=18,  # больше или равно 18
        le=120  # меньше или равно 120
    )]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
