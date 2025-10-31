from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com/'
soup = None
response = None

try:
    response = requests.get(url)
except Exception as e:
    print("An exception occurred related to HTTP request: ", e)


print('status code : ' + str(response.status_code))

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        rating_tag = book.find('p', class_='star-rating')

        # Достаём название рейтинга (One, Two, Three, Four, Five)
        rating_name = rating_tag['class'][1]

        # Преобразуем в число
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        rating = rating_map.get(rating_name, 0)

        # достаем изображение
        image_tag = book.find('img')
        image_src = image_tag['src']

        print(f"{title} : {price} : ⭐ {rating} : {image_src}")