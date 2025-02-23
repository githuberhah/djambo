import requests
from bs4 import BeautifulSoup

def scrape_books():
    url = "https://books.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']
        price = article.find('p', class_='price_color').text
        rating = article.p['class'][1]  # Пример: 'Three' для 3 звезд
        books.append({
            'title': title,
            'price': price,
            'rating': rating
        })
    return books
