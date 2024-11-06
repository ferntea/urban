import sqlite3

def initiate_db():
    """Creates the Products table if it doesn't exist."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,  -- Ensure title is unique
            description TEXT,
            price INTEGER NOT NULL,
            image BLOB
        )
    ''')
    connection.commit()
    connection.close()

def populate_db():
    """Populates the Products table with initial data if it's empty."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    products = [
        ("Помидоры",
         "много витамина А и витамина К, а также значительное количество витаминов группы В, фолиевой кислоты и "
         "тиамина. Один томат обеспечивает около 40% суточной потребности в витамине С. Также помидоры — хороший "
         "источник железа, калия, марганца, магния, фосфора и меди.",
         100, "image1.png"),
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
         400, "image4.png"),
    ]

    for title, description, price, image_path in products:
        # Check if the product already exists
        cursor.execute("SELECT COUNT(*) FROM Products WHERE title = ?", (title,))
        if cursor.fetchone()[0] == 0:  # If the product does not exist
            with open(image_path, 'rb') as file:
                image_data = file.read()  # Read the image file as binary
                cursor.execute('INSERT INTO Products (title, description, price, image) VALUES (?, ?, ?, ?)',
                               (title, description, price, image_data))
            print(f"Inserted {title} into the database.")
        else:
            print(f"{title} already exists in the database. Skipping insertion.")

    connection.commit()
    connection.close()


def get_all_products():
    """Returns all products from the Products table."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title, description, price, image FROM Products')  # Corrected column name
    products = cursor.fetchall()
    connection.close()
    return products