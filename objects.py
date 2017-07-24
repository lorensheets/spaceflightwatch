import requests
from bs4 import BeautifulSoup

def total():
    url = "http://www.unoosa.org/oosa/osoindex/search-ng.jspx?lf_id="
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    obj = soup.find('div', {'id': 'found-count'})
    return obj.string
