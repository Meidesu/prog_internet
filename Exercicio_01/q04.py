import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

links = soup.find_all('a')

for link in links:
    print(link.get('href'))
