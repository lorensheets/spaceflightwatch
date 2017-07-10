import urllib.request, json, ssl

context = ssl._create_unverified_context()

with urllib.request.urlopen("https://spaceinfo.herokuapp.com/spacexjobs",context=context) as url:
    data = json.loads(url.read().decode())
    for item in data:
        print(data[item])
