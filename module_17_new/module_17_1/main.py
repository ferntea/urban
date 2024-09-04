# module_17_1 Структура проекта. Маршруты и модели Pydantic

'''
Подготовка:

    Установите все необходимые библиотеки для дальнейшей работы: fastapi.
    Создайте файлы, структурировав из согласно рисунку:

    Задача "Основные маршруты":
Необходимо создать маршруты и написать Pydantic модели для дальнейшей работы.
Маршруты:
В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task', а также следующие маршруты, с пустыми функциями:

    get '/' с функцией all_tasks.
    get '/task_id' с функцией task_by_id.
    post '/create' с функцией create_task.
    put '/update' с функцией update_task.
    delete '/delete' с функцией delete_task.

В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user', а также следующие маршруты, с пустыми функциями:

    get '/' с функцией all_users.
    get '/user_id' с функцией user_by_id.
    post '/create' с функцией create_user.
    put '/update' с функцией update_user.
    delete '/delete' с функцией delete_user.

В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/', по которому функция возвращает словарь - {"message": "Welcome to Taskmanager"}.
Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI, объединив все маршруты в одно приложение.
Схемы:
Создайте 4 схемы в модуле schemas.py, наследуемые от BaseModel, для удобной работы с будущими объектами БД:

    CreateUser с атрибутами: username(str), firstname(str), lastname(str) и age(int)
    UpdateUser с атрибутами: firstname(str), lastname(str) и age(int)
    CreateTask с атрибутами: title(str), content(str), priority(int)
    UpdateTask с теми же атрибутами, что и CreateTask.

Обратите внимание, что 1/2 и 3/4 схемы обладают одинаковыми атрибутами.

Таким образом вы получите подготовленные маршруты и схемы для дальнейшего описания вашего API.
'''

from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

# app.include_router(task_router, prefix="/tasks")
# app.include_router(user_router, prefix="/users")

app.include_router(task_router)
app.include_router(user_router)