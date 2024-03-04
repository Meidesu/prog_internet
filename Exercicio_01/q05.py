import requests
from bs4 import BeautifulSoup

url = input('Digite a URL: ')

response = requests.get(url)

