import requests
from bs4 import BeautifulSoup

URL = 'https://improvado.io/blog'
HOST = 'https://improvado.io/'


def get_html(url):
    response = requests.get(url)
    return response


def get_links(html):
    soup = BeautifulSoup(html.text, 'lxml')
    items = soup.find_all(
        'div',
        class_='collection-item-5 w-dyn-item w-col w-col-6',
        limit=20)
    links = []
    for item in items:
        links.append(
            HOST + item.find(
                'a',
                class_='link-block-12 w-inline-block').get('href')
        )
    return links


def text_to_files(links):
    for item in links:
        r = get_html(item).text
        soup = BeautifulSoup(r, 'lxml')
        data = soup.find('div', class_='c-rich-text-blog w-richtext')
        with open("data.txt", "a") as file:
            file.write(data.text)
        print('текст записан')


text_to_files(get_links(get_html(URL)))
