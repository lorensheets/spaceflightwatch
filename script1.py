from flask import Flask, render_template
import nextlaunch, urllib.request, json

app=Flask(__name__)

@app.route('/')
def home():
    launch = nextlaunch.getnext()
    upcoming = nextlaunch.upcoming()
    #spacexjobs = jobs.spacex()
    #blueoriginjobs = jobs.blueorigin()
    #phasefourjobs = jobs.phasefour()
    #rocketlabsjobs = jobs.rocketlabs()
    #bigelowjobs = jobs.bigelow()

    with urllib.request.urlopen("https://spaceinfo.herokuapp.com/spacexjobs.html") as url:
        spacexjobs = json.loads(url.read().decode())

    planetaryresourcesjobs = [['Finance & Operations Analyst','?gh_jid=744711'], \
        ['Chief Scientist','?gh_jid=682831'], \
        ['Director of Instrument Systems','?gh_jid=682839'], \
        ['Early Career Engineer','?gh_jid=682849'], \
        ['Instrument Systems Engineer','?gh_jid=745216'], \
        ['Mission Design Engineer','?gh_jid=647441'], \
        ['Network Engineer','?gh_jid=682858'], \
        ['Planetary Scientist','?gh_jid=682861'], \
        ['Propulsion System Engineer','?gh_jid=682863'], \
        ['Senior Instrument Systems Engineer','?gh_jid=745263'], \
        ['Thermal Subsystems Engineer','?gh_jid=745158'], \
        ['Mission Design Engineer, Luxembourg','?gh_jid=716075'], \
        ['Planetary Scientist - Luxembourg','?gh_jid=716052'], \
        ['Business Analyst','?gh_jid=744045'], \
        ['Director of Marketing','?gh_jid=682845']]

    return render_template("index.html", time=launch[0],
    next=launch[1], link=launch[2], date=launch[3], upcoming=upcoming,
    spacexjobs=spacexjobs, blueoriginjobs=blueoriginjobs, phasefourjobs=phasefourjobs,
    rocketlabsjobs=rocketlabsjobs, planetaryresourcesjobs=planetaryresourcesjobs,
    bigelowjobs=bigelowjobs)

if __name__=="__main__":
    app.run(debug=True)

@app.route('/jsondata')
def data():
    return render_template("json.html")
