# module_14_3_new Доработка бота.

'''
Задача "Витамины для всех!":
Подготовка:
Подготовьте Telegram-бота из последнего домашнего задания 13 моудля сохранив код с ним в файл module_14_3.py.
Если вы не решали новые задания из предыдущего модуля рекомендуется выполнить их.

Дополните ранее написанный код для Telegram-бота:
Создайте и дополните клавиатуры:

    В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
    Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4". У всех кнопок
    назначьте callback_data="product_buying"

Создайте хэндлеры и функции к ним:

    Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
    Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number> | Цена:
    <number * 100>' 4 раза. После каждой надписи выводите картинки к продуктам. В конце выведите ранее созданное
    Inline меню с надписью "Выберите продукт для покупки:".
    Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
    Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"
'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import API

API_TOKEN = API

# Инициализация
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_calculate = types.KeyboardButton("Рассчитать")
    button_info = types.KeyboardButton("Информация")
    keyboard.add(button_calculate, button_info)     # two buttons
    button_buy = types.KeyboardButton("Купить")         # one wide button
    keyboard.add(button_buy)
    return keyboard


def create_inline_keyboard_calc():
    inline_keyboard = types.InlineKeyboardMarkup()
    button_calories = types.InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories')
    button_formulas = types.InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
    inline_keyboard.add(button_calories, button_formulas)
    return inline_keyboard

def create_inline_keyboard_prods():
    inline_keyboard = types.InlineKeyboardMarkup(row_width=4)
    button_product1 = types.InlineKeyboardButton("Помидоры", callback_data='product1_buying')
    button_product2 = types.InlineKeyboardButton("Чеснок", callback_data='product2_buying')
    button_product3 = types.InlineKeyboardButton("Баклажаны", callback_data='product3_buying')
    button_product4 = types.InlineKeyboardButton("Морковь", callback_data='product4_buying')

    inline_keyboard.add(button_product1, button_product2, button_product3, button_product4)
    return inline_keyboard      # there was a mistake, it was return inline_keyboards_prods, difficult to find!!!

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=create_keyboard())

@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=create_inline_keyboard_calc())

@dp.message_handler(lambda message: message.text.lower() == 'информация')
async def info_menu(message: types.Message):
    await message.answer("Это бот по задаче module_14_3 для вычисления потребности в калориях для мужчин и покупки "
                         "некоторых продуктов, содержащих витамины ")

@dp.message_handler(lambda message: message.text.lower() == 'купить')
async def get_buying_list(message: types.Message):
    try:
        products = [
            ("Помидоры",
             "много витамина А и витамина К, а также значительное количество витаминов группы В, фолиевой кислоты и "
             "тиамина. Один томат обеспечивает около 40% суточной потребности в витамине С. Также помидоры — хороший "
             "источник железа, калия, марганца, магния, фосфора и меди.",
             100, "image1.png"),      # used in a simplest way without using a list
            ("Чеснок",
             "Чеснок содержит такие витамины, как C, B6, B1, B2, B3, B5, B9, а также полезные микроэлементы: кальций, "
             "калий, фосфор, селен, магний, натрий, цинк, железо и марганец. Эфирное масло чеснока – аллицин, является "
             "мощным антиоксидантом. Калорийность чеснока - 149 калорий на 100 грамм продукта.",
             200, "image2.png"),
            ("Баклажаны",
             "В составе баклажана большое количество витаминов, в том числе C и B6, фолиевая кислота, каротин, а также "
             "микроэлементы: калий, кальций, железо, медь, цинк и др. Высокое содержание в баклажанах солей калия "
             "оказывает положительное влияние на работу сердца и способствует выведению из организма лишних жидкостей.",
             300, "image3.png"),
            ("Морковь",
             "Так, в моркови содержатся витамины PP, A, B1, B2, B5, B6, B9, C, E, H и K, а также железо, цинк, йод, "
             "медь, марганец, селен, хром, фтор, молибден, бор, ванадий, кобальт, литий, алюминий, никель, кальций, "
             "магний, натрий, калий, фосфор, хлор и сера. Кроме того, морковь не калорийна – всего 35 килокалорий "
             "на 100 граммов.",
             400, "image4.png")
        ]

        for name, desc, price, img in products:
            # Send the product information as a message
            await message.answer(f"{name}: {desc} - {price}₽")
            # Send the associated image
            with open(img, 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo)     # ensure the file is closed after sending

        await message.answer("Выберите продукт для покупки:", reply_markup=create_inline_keyboard_prods())
    except Exception as e:
        await message.answer(f"An error occurred: {str(e)}")


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('product'))
async def process_product_selection(callback_query: types.CallbackQuery):
    product_mapping = {
        'product1_buying': 'Помидоры',
        'product2_buying': 'Чеснок',
        'product3_buying': 'Баклажаны',
        'product4_buying': 'Морковь'
    }

    product_name = product_mapping.get(callback_query.data)
    if product_name:
        await bot.answer_callback_query(callback_query.id)  # Acknowledge the callback
        await bot.send_message(callback_query.from_user.id, f"Вы выбрали {product_name}. Спасибо за покупку!")
    else:
        await bot.answer_callback_query(callback_query.id, text="Неизвестный продукт.")

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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
