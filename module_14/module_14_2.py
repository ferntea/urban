# module_14_2 Регулярные выражения.

'''
Задание:

Разработайте функцию для извлечения информации из HTML-текста (строки Python) о ссылках на изображения (URL-адресах картинок). Функция должна находить все ссылки на изображения в форматах JPEG, JPG, PNG или GIF и возвращать их список.

1. Создайте функцию extract_image_links(html_text), которая принимает HTML-текст и извлекает ссылки на изображения.
2. Используйте регулярные выражения для поиска URL-адресов картинок с расширениями .jpg, .jpeg, .png или .gif.
3. Верните список всех найденных ссылок на изображения.


Пример работы функции:


sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"

image_links = extract_image_links(sample_html)
if image_links:
  for image_link in image_links:
    print(image_link)
else:
  print("Нет ссылок с картинками в HTML тексте.")

Вывод на консоль:
https://example.com/image1.jpg
http://example.com/image2.png
https://example.com/image3.gif

Примечания:

    Вам могут понадобиться следующие спец. символы: / ? [] | +
    Учтите что 'http' это подстрока строки 'https'.
'''

import re

def extract_image_links(html_text):
    # Регулярное выражение для поиска ссылок на изображения
    pattern = r'<img[^>]+src=[\'"]?(https?://[^\'" >]+(?:\.jpg|\.jpeg|\.png|\.gif))[\'"]?'
    # Найти все совпадения
    image_links = re.findall(pattern, html_text, re.IGNORECASE)
    return image_links

# Пример использования функции
sample_html = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> "
               "<img src='https://example.com/image3.gif'>")

image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")