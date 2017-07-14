import requests
from bs4 import BeautifulSoup

def getnews():
    url = ""
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
