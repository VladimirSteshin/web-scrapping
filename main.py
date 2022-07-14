import bs4
import configparser
import requests
from fake_headers import Headers


def get_url_and_keywords(file):
    config = configparser.ConfigParser()
    config.read(file, encoding='UTF-8')
    BASE_URL = config['URL']['base_url']
    WORK_URL = config['URL']['work_url']
    KEYWORDS = config['KEYWORDS']['keywords']
    KEYWORDS = KEYWORDS.split(', ')
    return BASE_URL, WORK_URL, KEYWORDS


def get_headers():
    HEADERS = Headers(headers=True)
    HEADERS = HEADERS.generate()
    return HEADERS


def get_response(path, params):
    response = requests.get(path, headers=params)
    data = response.text
    return data


def get_articles(data, check, path):
    soup = bs4.BeautifulSoup(data, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        preview = article.find_all(class_='article-formatted-body')
        for info in preview:
            data = info.text.lower()
            for word in check:
                if word.lower() in data:
                    found_time = article.find('time').attrs['title'].split(', ')[0]
                    found_name = article.find(class_='tm-article-snippet__title-link').text
                    found_href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                    print(f'{found_time} {found_name} {path + found_href}')
                    break


if __name__ == "__main__":
    base_url, work_url, keywords = get_url_and_keywords('config.ini')
    headers = get_headers()
    text = get_response(work_url, headers)
    get_articles(text, keywords, base_url)
