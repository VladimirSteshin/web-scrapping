import bs4
import configparser
import requests
from fake_headers import Headers


def get_url(file):
    config = configparser.ConfigParser()
    config.read(file)
    URL = config['URL']['url']
    return URL


def get_headers():
    HEADERS = Headers(headers=True)
    HEADERS = HEADERS.generate()
    return HEADERS


if __name__ == "__main__":
    url = get_url('config.ini')
    headers = get_headers()
    print(url)
    print(headers)
    