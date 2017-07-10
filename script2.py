import urllib.request, json

with urllib.request.urlopen("https://spaceinfo.herokuapp.com/spacexjobs.html") as url:
    data = json.loads(url.read().decode())
    print(data)
