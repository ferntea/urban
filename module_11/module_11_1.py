# Обзор сторонних библиотек Python

'''
Задача:

    Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
    После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями. К каждой библиотеке дана ссылка на документацию ниже.

Если вы выбрали:

    requests - запросить данные с сайта и вывести их в консоль.
    pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
    numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
    matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
    pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.

В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека и как вы расширили возможности Python с её помощью.
Примечания:

    Можете выбрать не более 3-х библиотек для изучения.
    Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.
'''

# Pandas
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

print('\nPandas')
print(df.head())
print(df.info())

filtered_df = df[df['Age'] > 30]
print(filtered_df)


# Numpy
import numpy as np

arr = np.arange(1, 9)           # Generate 8 elements

print('\nNumpy')
print('Sum:', np.sum(arr))
print('Mean:', np.mean(arr))
print('Max:', np.max(arr))

print('array:', arr)
reshaped_arr = arr.reshape(2, 4)        # 2 rows, 4 columns
print('Reshaped array (2 row, 4 columns:\n', reshaped_arr)

reshaped_arr = arr.reshape(4, 2)        # 4 rows, 2 columns
print('Reshaped array (4 row, 2 columns:\n', reshaped_arr)


# Matplotlib
import matplotlib.pyplot as plt

# Data for the x and y coordinates
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 16]

# Create a line plot
plt.plot(x, y, marker='o', color='red')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My Test Plot')

plt.savefig('module_11_1_test_plot.png')   # save to directory

plt.show()      # show on the screen