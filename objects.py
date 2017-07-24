import requests
from bs4 import BeautifulSoup

def total():
    url = "http://www.unoosa.org/oosa/osoindex/search-ng.jspx?lf_id="
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for obj in soup.findAll('div', {'id': 'found-count'}):
        return obj.string
