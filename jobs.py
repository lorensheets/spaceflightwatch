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
    file = open("templates/spacexjobs.html","w")
    file.write("{\n")
    file.close()
    for tables in soup.findAll('table', {'class': 'views-table'}):
        category = tables.find('div', {'class': 'field-name-field-job-category'})
        file = open("templates/spacexjobs.html","a")
        file.write("\"" + category.string.strip() + "\":[{\n")
        file.close()
        for jobs in tables.findAll('a',href=True):
            job = jobs.string
            joblink = jobs['href']
            file = open("templates/spacexjobs.html","a")
            file.write("\"" + job + "\":\"" + joblink + "\",\n")
            file.close()
            #spacex_results.append([job,joblink])
        file = open("templates/spacexjobs.html","a")
        file.write("}],\n")
        file.close()
    file = open("templates/spacexjobs.html","r")
    lines = file.readlines()
    lines[len(lines)-1] = lines[len(lines)-1][:-2]
    file.close()
    file = open("templates/spacexjobs.html","w")
    file.writelines(lines)
    file.close()
    file = open("templates/spacexjobs.html","a")
    file.write("}")
    file.close()

    #return spacex_results

def blueorigin():
    url = "https://www.blueorigin.com/careers"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    file = open("templates/blueoriginjobs.html","w")
    file.write("{\n")
    file.close()
    for items in soup.findAll('a', {'class': 'job-entry'}):
        joblink = items['href']
        job = items.find('div', {'class': 'job-title'})
        file = open("templates/blueoriginjobs.html","a")
        file.write("\"" + job.string + "\":\"" + joblink + "\",\n")
        file.close()
        #blueorigin_results.append([job.string,joblink])
    file = open("templates/blueoriginjobs.html","r")
    lines = file.readlines()
    lines[len(lines)-1] = lines[len(lines)-1][:-2]
    file.close()
    file = open("templates/blueoriginjobs.html","w")
    file.writelines(lines)
    file.close()
    file = open("templates/blueoriginjobs.html","a")
    file.write("}")
    file.close()
    #return blueorigin_results


def phasefour():
    url = "http://www.phasefour.io/careers/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    file = open("templates/phasefourjobs.html","w")
    file.write("{\n")
    file.close()
    for items in soup.findAll('a', {'class': 'custom-link'}):
        job = items.string
        joblink = items['href']
        file = open("templates/phasefourjobs.html","a")
        file.write("\"" + job + "\":\"" + joblink + "\",\n")
        file.close()
        #phasefour_results.append([job,joblink])
    file = open("templates/phasefourjobs.html","r")
    lines = file.readlines()
    lines[len(lines)-1] = lines[len(lines)-1][:-2]
    file.close()
    file = open("templates/phasefourjobs.html","w")
    file.writelines(lines)
    file.close()
    file = open("templates/phasefourjobs.html","a")
    file.write("}")
    file.close()
    #return phasefour_results

def rocketlabs():
    url = "https://www.rocketlabusa.com/careers/positions/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    file = open("templates/rocketlabsjobs.html","w")
    file.write("{\n")
    file.close()
    for items in soup.findAll('article', {'class': 'job__container'}):
        item = items.find('a', {'class': 'job'})
        job = item.find('h3')
        joblink = item['href']
        file = open("templates/rocketlabsjobs.html","a")
        file.write("\"" + job.string + "\":\"" + joblink + "\",\n")
        file.close()
        #rocketlabs_results.append([job.string,joblink])
    file = open("templates/rocketlabsjobs.html","r")
    lines = file.readlines()
    lines[len(lines)-1] = lines[len(lines)-1][:-2]
    file.close()
    file = open("templates/rocketlabsjobs.html","w")
    file.writelines(lines)
    file.close()
    file = open("templates/rocketlabsjobs.html","a")
    file.write("}")
    file.close()
    #return rocketlabs_results


def bigelow():
    url = "http://www.bigelowaerospace.com/job-opportunities/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    file = open("templates/bigelowjobs.html","w")
    file.write("{\n")
    file.close()
    for items in soup.findAll('td'):
        for jobs in items.findAll('a'):
            job = jobs.text.strip()
            joblink = jobs['href'].strip()
            file = open("templates/bigelowjobs.html","a")
            file.write("\"" + job + "\":\"" + joblink + "\",\n")
            file.close()
            #bigelow_results.append([job,joblink])
    file = open("templates/bigelowjobs.html","r")
    lines = file.readlines()
    lines[len(lines)-1] = lines[len(lines)-1][:-2]
    file.close()
    file = open("templates/bigelowjobs.html","w")
    file.writelines(lines)
    file.close()
    file = open("templates/bigelowjobs.html","a")
    file.write("}")
    file.close()
    #return bigelow_results


spacex()
blueorigin()
phasefour()
rocketlabs()
bigelow()
