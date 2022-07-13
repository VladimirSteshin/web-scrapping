import bs4
import configparser
import requests
from fake_headers import Headers


def get_url_and_keywords(file):
    config = configparser.ConfigParser()
    config.read(file, encoding='UTF-8')
    URL = config['URL']['url']
    KEYWORDS = config['KEYWORDS']['keywords']
    KEYWORDS = KEYWORDS.split(', ')
    return URL, KEYWORDS


def get_headers():
    HEADERS = Headers(headers=True)
    HEADERS = HEADERS.generate()
    return HEADERS


def get_response(path, params):
    response = requests.get(path, headers=params)
    data = response.text
    return data


def get_articles(data):
    soup = bs4.BeautifulSoup(data, features='html.parser')
    item = soup.find_all('article')
    return item


def find_coincidences(articles_found, keywords):
    for article in articles_found:
        preview = article.find_all(class_='tm-article-body tm-article-snippet__lead')
        print()


if __name__ == "__main__":
    url, keywords = get_url_and_keywords('config.ini')
    headers = get_headers()
    text = get_response(url, headers)
    articles = get_articles(text)
    result = find_coincidences(articles, keywords)
