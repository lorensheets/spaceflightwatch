import requests
from bs4 import BeautifulSoup

spacex_results = []
blueorigin_results = []
phasefour_results = []
rocketlabs_results = []
bigelow_results = []

def spacex():
    url = "https://spacex.com/careers/list"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for tables in soup.findAll('table', {'class': 'views-table'}):
        for jobs in tables.findAll('a',href=True):
            job = jobs.string
            joblink = jobs['href']
            spacex_results.append([job,joblink])
    return spacex_results

def blueorigin():
    url = "https://www.blueorigin.com/careers"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for items in soup.findAll('a', {'class': 'job-entry'}):
        joblink = items['href']
        job = items.find('div', {'class': 'job-title'})
        blueorigin_results.append([job.string,joblink])
    return blueorigin_results


def phasefour():
    url = "http://www.phasefour.io/careers/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for items in soup.findAll('a', {'class': 'custom-link'}):
        job = items.string
        joblink = items['href']
        phasefour_results.append([job,joblink])
    return phasefour_results

def rocketlabs():
    url = "https://www.rocketlabusa.com/careers/positions/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for items in soup.findAll('article', {'class': 'job__container'}):
        item = items.find('a', {'class': 'job'})
        job = item.find('h3')
        joblink = item['href']
        rocketlabs_results.append([job.string,joblink])
    return rocketlabs_results


def bigelow():
    url = "http://www.bigelowaerospace.com/job-opportunities/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for items in soup.findAll('td'):
        for jobs in items.findAll('a'):
            job = jobs.text.strip()
            joblink = jobs['href'].strip()
            bigelow_results.append([job,joblink])
    return bigelow_results
