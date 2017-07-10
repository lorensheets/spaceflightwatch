import urllib.request, json, ssl

context = ssl._create_unverified_context()

with urllib.request.urlopen("https://spaceinfo.herokuapp.com/spacexjobs",context=context) as url:
    data = json.loads(url.read().decode())
    print(data)
