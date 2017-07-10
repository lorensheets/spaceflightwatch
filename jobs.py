import requests
from bs4 import BeautifulSoup

#spacex_results = []
#blueorigin_results = []
#phasefour_results = []
#rocketlabs_results = []
#bigelow_results = []

def spacex():
    url = "https://spacex.com/careers/list"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    file = open("spacexjobs.html","w")
    file.write("{\n")
    file.close()
    for tables in soup.findAll('table', {'class': 'views-table'}):
        for jobs in tables.findAll('a',href=True):
            job = jobs.string
            joblink = jobs['href']
            file = open("spacexjobs.html","a")
            file.write("\"" + job + "\":\"" + joblink + "\",\n")
            file.close()
            #spacex_results.append([job,joblink])
    file = open("spacexjobs.html","a")
    file.write("}")
    file.close()
    #return spacex_results

def blueorigin():
    url = "https://www.blueorigin.com/careers"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    file = open("blueoriginjobs.html","w")
    file.write("{\n")
    file.close()
    for items in soup.findAll('a', {'class': 'job-entry'}):
        joblink = items['href']
        job = items.find('div', {'class': 'job-title'})
        file = open("blueoriginjobs.html","a")
        file.write("\"" + job.string + "\":\"" + joblink + "\",\n")
        file.close()
        #blueorigin_results.append([job.string,joblink])
    file = open("blueoriginjobs.html","a")
    file.write("}")
    file.close()
    #return blueorigin_results


def phasefour():
    url = "http://www.phasefour.io/careers/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    file = open("phasefourjobs.html","w")
    file.write("{\n")
    file.close()
    for items in soup.findAll('a', {'class': 'custom-link'}):
        job = items.string
        joblink = items['href']
        file = open("phasefourjobs.html","a")
        file.write("\"" + job + "\":\"" + joblink + "\",\n")
        file.close()
        #phasefour_results.append([job,joblink])
    file = open("phasefourjobs.html","a")
    file.write("}")
    file.close()
    #return phasefour_results

def rocketlabs():
    url = "https://www.rocketlabusa.com/careers/positions/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    file = open("rocketlabsjobs.html","w")
    file.write("{\n")
    file.close()
    for items in soup.findAll('article', {'class': 'job__container'}):
        item = items.find('a', {'class': 'job'})
        job = item.find('h3')
        joblink = item['href']
        file = open("rocketlabsjobs.html","a")
        file.write("\"" + job.string + "\":\"" + joblink + "\",\n")
        file.close()
        #rocketlabs_results.append([job.string,joblink])
    file = open("rocketlabsjobs.html","a")
    file.write("}")
    file.close()
    #return rocketlabs_results


def bigelow():
    url = "http://www.bigelowaerospace.com/job-opportunities/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    file = open("bigelowjobs.html","w")
    file.write("{\n")
    file.close()
    for items in soup.findAll('td'):
        for jobs in items.findAll('a'):
            job = jobs.text.strip()
            joblink = jobs['href'].strip()
            file = open("bigelowjobs.html","a")
            file.write("\"" + job + "\":\"" + joblink + "\",\n")
            file.close()
            #bigelow_results.append([job,joblink])
    file = open("bigelowjobs.html","a")
    file.write("}")
    file.close()
    #return bigelow_results


spacex()
blueorigin()
phasefour()
rocketlabs()
bigelow()
