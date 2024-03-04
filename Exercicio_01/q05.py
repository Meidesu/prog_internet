import requests
from bs4 import BeautifulSoup

url = input('Digite a URL: ')
text = input('Texto:')

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

ocorrencias = soup.find_all_previous(name=True, string=text, limit=10)

print(ocorrencias)

for ocurr in ocorrencias:
    print(ocurr.text)