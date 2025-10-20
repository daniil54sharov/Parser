from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = None

print('status code : ' + str(response.status_code))

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    for book in soup.find_all('article', class_ = 'product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_ = 'price_color').text
        rating = 0
        for star in book.find('p', class_ = 'star-rating Three'):
            i_item = star.find('i', class_ = 'icon-star')
            rating += 1
        print(title, price, "rating", rating, sep = ' : ', end = '\n')