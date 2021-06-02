from bs4 import BeautifulSoup

import requests

site = requests.get("https://wwww.google.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())

