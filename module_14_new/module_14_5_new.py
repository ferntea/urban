# module_14_5_new Написание примитивной ORM

'''
Задача "Регистрация покупателей":
Подготовка:
Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.

Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:

    id - целое число, первичный ключ
    username - текст (не пустой)
    email - текст (не пустой)
    age - целое число (не пустой)
    balance - целое число (не пустой)

add_user(username, email, age), которая принимает: имя пользователя, почту и возраст. Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными. Баланс у новых пользователей всегда равен 1000. Для добавления записей в таблице используйте SQL запрос.
is_included(username) принимает имя пользователя и возвращает True, если такой пользователь есть в таблице Users, в противном случае False. Для получения записей используйте SQL запрос.

Изменения в Telegram-бот:

    Кнопки главного меню дополните кнопкой "Регистрация".
    Напишите новый класс состояний RegistrationState с следующими объектами класса State: username, email, age, balance(по умолчанию 1000).
    Создайте цепочку изменений состояний RegistrationState.

Фукнции цепочки состояний RegistrationState:
sing_up(message):

    Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
    Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
    После ожидать ввода имени в атрибут RegistrationState.username при помощи метода set.

set_username(message, state):

    Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
    Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на message.text. Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
    Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя" и запрашивать новое состояние для RegistrationState.username.

set_email(message, state):

    Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
    Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
    Далее выводить сообщение "Введите свой возраст:":
    После ожидать ввода возраста в атрибут RegistrationState.age.

set_age(message, state):

    Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
    Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
    Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users при помощи ранее написанной crud-функции add_user.
    В конце завершать приём состояний при помощи метода finish().

Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.
'''


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import API
from module_14_5_crud_functions import initiate_db, populate_db, add_user, is_included, get_all_products

API_TOKEN = API

# Инициализация
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    username = State()
    email = State()

# Add a new state for registration
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    username = State()
    email = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = types.KeyboardButton("Рассчитать")
    button_info = types.KeyboardButton("Информация")
    button_register = types.KeyboardButton("Регистрация")  # Add Registration button
    keyboard.add(button_calculate, button_info, button_register)  # Add the button to the keyboard
    button_buy = types.KeyboardButton("Купить")
    keyboard.add(button_buy)
    return keyboard

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=create_keyboard())

@dp.message_handler(lambda message: message.text.lower() == 'регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        user_data = await state.get_data()
        username = user_data.get('username')
        email = user_data.get('email')

        # Add user to the database
        add_user(username, email, age)
        await message.answer("Вы успешно зарегистрированы!")
        await state.finish()  # Finish the registration process
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст.")

def create_inline_keyboard_calc():
    inline_keyboard = types.InlineKeyboardMarkup()
    button_calories = types.InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories')
    button_formulas = types.InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
    inline_keyboard.add(button_calories, button_formulas)
    return inline_keyboard

def create_inline_keyboard_prods(products):
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    for product in products:
        title = product[0]  # Assuming title is the first element
        callback_data = f'buy_{title}'  # Create callback data based on title
        button = types.InlineKeyboardButton(title, callback_data=callback_data)
        inline_keyboard.add(button)
    return inline_keyboard

@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=create_inline_keyboard_calc())


@dp.message_handler(lambda message: message.text.lower() == 'информация')
async def info_menu(message: types.Message):
    await message.answer("Это бот по задаче module_14_5 с примитивной ORM "
                         "на основе предыдущих заданий module_13_6, module_14_3 и module_14_4")


@dp.message_handler(lambda message: message.text.lower() == 'купить')
async def get_buying_list(message: types.Message):
    try:
        products = get_all_products()  # Fetch products from the database

        for title, description, price, image_data in products:
            # Send the product information as a message
            await message.answer(f"Название: {title} | Описание: {description} | Цена: {price}₽")
            # Send the associated image if it exists
            if image_data:
                await bot.send_photo(chat_id=message.chat.id, photo=image_data)

        await message.answer("Выберите продукт для покупки:", reply_markup=create_inline_keyboard_prods(products))
    except Exception as e:
        await message.answer(f"An error occurred: {str(e)}")


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('buy_'))
async def process_product_selection(callback_query: types.CallbackQuery):
    # Extract the product name from the callback data
    product_name = callback_query.data.split('_', 1)[1].strip()  # Get the product name after 'buy_'

    # Check if the product exists in the database
    if product_exists(product_name):
        await bot.answer_callback_query(callback_query.id)  # Acknowledge the callback
        await bot.send_message(callback_query.from_user.id, f"Вы выбрали {product_name}. Спасибо за покупку!")
    else:
        await bot.answer_callback_query(callback_query.id, text="Неизвестный продукт.")

def product_exists(product_name: str) -> bool:
    """Check if the product exists in the database."""
    products = get_all_products()
    return any(product_name.lower() == product[0].strip().lower() for product in products)


@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_message = (
        "Формула Миффлина - Сан Жеора для мужчин:\n"
        "BMR = 10 * вес + 6.25 * рост - 5 * возраст + 5"
    )
    await call.message.answer(formula_message)
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        await state.update_data(age=age)
        await message.answer("Введите свой рост в см:")
        await UserState.growth.set()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст.")


@dp.message_handler(state=UserState.growth)
async def process_growth(message: types.Message, state: FSMContext):
    try:
        growth = int(message.text)
        await state.update_data(growth=growth)
        await message.answer("Введите свой вес в кг:")
        await UserState.weight.set()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный рост.")


@dp.message_handler(state=UserState.weight)
async def process_weight(message: types.Message, state: FSMContext):
    try:
        weight = int(message.text)
        user_data = await state.get_data()
        age = user_data.get('age')
        growth = user_data.get('growth')

        # Here you can calculate BMR or handle the data as needed
        await message.answer(f"Ваши данные:\nВозраст: {age}\nРост: {growth}\nВес: {weight}")

        # Формула Миффлина - Сан Жеора для мужчин: BMR = 10 * weight + 6.25 * height - 5 * age + 5
        calories = 10 * weight + 6.25 * growth - 5 * age + 5

        await message.answer(f"Ваша норма калорий: {calories:.2f} ккал в день.")

        await state.finish()  # Завершение машины состояний
        await state.finish()  # Reset the state after processing
    except ValueError:
        await message.answer("Пожалуйста, введите корректный вес.")


@dp.message_handler(lambda message: message.text.lower() == 'регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        user_data = await state.get_data()
        username = user_data.get('username')
        email = user_data.get('email')

        # Add user to the database
        add_user(username, email, age)
        await message.answer("Вы успешно зарегистрированы!")
        await state.finish()  # Finish the registration process
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст.")


if __name__ == '__main__':
    initiate_db()  # Initialize the database
    populate_db()  # Populate the database with initial data
    executor.start_polling(dp, skip_updates=True)  # Start the bot
