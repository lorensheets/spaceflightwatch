import requests
from bs4 import BeautifulSoup

launch_dates = []
launch_times = []
launch_titles = []
launch_site = []

def launches():
    url = "https://spaceflightnow.com/launch-schedule/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for launch in soup.findAll('div', {'class': 'datename'}):
        title = launch.find('span', {'class': 'mission'})
        launch_titles.append(title.string)
    return launch_titles

def dates():
    url = "https://spaceflightnow.com/launch-schedule/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for launch in soup.findAll('div', {'class': 'datename'}):
        date = launch.find('span', {'class': 'launchdate'})
        launch_dates.append(date.string)
    return launch_dates


def times():
    url = "https://spaceflightnow.com/launch-schedule/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for launch in soup.findAll('div', {'class': 'missiondata'}):
        txt = launch.text
        txt = txt.split("Launch site: ")
        txt = txt[0].split(": ")
        launch_times.append(txt[1].strip())

    return launch_times

def sites():
    url = "https://spaceflightnow.com/launch-schedule/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for launch in soup.findAll('div', {'class': 'missiondata'}):
        txt = launch.text
        txt = txt.split("Launch site: ")
        launch_site.append(txt[1].strip())

    return launch_site
