from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET

url = 'https://books.toscrape.com/'
soup = None
response = None
root = ET.Element('book_catalog')
id_count = 0

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
        image_address = None
        image_tag = book.find('img')
        image_src = image_tag.get('src')
        if image_src: # Check if src attribute exists
            image_address = image_src

        id_xml = ET.SubElement(root, 'book', id = str(id_count))
        title_xml = ET.SubElement(id_xml, 'title', book_title = title)
        price_xml = ET.SubElement(id_xml, 'price', book_price = price)
        image_src_xml = ET.SubElement(id_xml, 'image', book_image_src = 'https://books.toscrape.com/' + image_address)
        rating_xml = ET.SubElement(id_xml, 'rating', book_rating = str(rating))

        id_count += 1
else:
    print('Failed to parse data')

tree = ET.ElementTree(root)
ET.indent(tree)
tree.write('books.xml', encoding='utf-8', xml_declaration=True)