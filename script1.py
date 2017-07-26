from flask import Flask, render_template
import nextlaunch, urllib.request, json, ssl

app=Flask(__name__)

@app.route('/')
def home():

    #next launch
    with urllib.request.urlopen("http://spaceflight.watch/nextlaunch") as url:
        nextlaunch = json.loads(url.read().decode())

    #upcoming launches
    with urllib.request.urlopen("http://spaceflight.watch/upcominglaunches") as url:
        upcoming = json.loads(url.read().decode())

    #launch = nextlaunch.getnext()
    #upcoming = nextlaunch.upcoming()

    return render_template("index.html", date=nextlaunch[3],time=nextlaunch[0],
        link=nextlaunch[2],next=nextlaunch[1],upcoming=upcoming)

@app.route('/jobs')
def jobs():

    #context = ssl._create_unverified_context()

    #spacex jobs
    with urllib.request.urlopen("http://spaceflight.watch/spacexjobs") as url:
        spacexjobs = json.loads(url.read().decode())

    #blueorigin jobs
    with urllib.request.urlopen("http://spaceflight.watch/blueoriginjobs") as url:
        blueoriginjobs = json.loads(url.read().decode())

    #phasefour jobs
    with urllib.request.urlopen("http://spaceflight.watch/phasefourjobs") as url:
        phasefourjobs = json.loads(url.read().decode())

    #rocketlabs jobs
    with urllib.request.urlopen("http://spaceflight.watch/rocketlabsjobs") as url:
        rocketlabsjobs = json.loads(url.read().decode())

    #bigelow jobs
    with urllib.request.urlopen("http://spaceflight.watch/bigelowjobs") as url:
        bigelowjobs = json.loads(url.read().decode())

    #moon express jobs
    with urllib.request.urlopen("http://spaceflight.watch/moonexpressjobs") as url:
        moonexpressjobs = json.loads(url.read().decode())

    #planet labs jobs
    with urllib.request.urlopen("http://spaceflight.watch/planetlabsjobs") as url:
        planetlabsjobs = json.loads(url.read().decode())

    planetaryresourcesjobs = [
        ['Finance & Operations Analyst','?gh_jid=744711'], \
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
        ['Director of Marketing','?gh_jid=682845']
    ]

    vectorspacesystemsjobs = [
        ['Ground Software Engineer','/job/ground-software-engineer/'], \
        ['Electrical Wiring Technician','/job/electrical-wiring-technician/'], \
        ['Embedded Software Engineer','/job/embedded-software-engineer/']
    ]

    return render_template("jobs.html", spacexjobs=spacexjobs, blueoriginjobs=blueoriginjobs,
        phasefourjobs=phasefourjobs, planetaryresourcesjobs=planetaryresourcesjobs,
        rocketlabsjobs=rocketlabsjobs, bigelowjobs=bigelowjobs, moonexpressjobs=moonexpressjobs,
        planetlabsjobs=planetlabsjobs,vectorspacesystemsjobs=vectorspacesystemsjobs)

@app.route('/news')
def news():
    return render_template("spacenews.html")



if __name__=="__main__":
    app.run(debug=True)

#render next launch json
@app.route('/nextlaunch')
def nextlaunch():
    return render_template("nextlaunch.html")

#render upcoming launches json
@app.route('/upcominglaunches')
def upcoming():
    return render_template("upcominglaunches.html")

#render spacexjobs json
@app.route('/spacexjobs')
def spacexjobs():
    return render_template("spacexjobs.html")

#render blueoriginjobs json
@app.route('/blueoriginjobs')
def blueoriginjobs():
    return render_template("blueoriginjobs.html")

#render phasefourjobs json
@app.route('/phasefourjobs')
def phasefourjobs():
    return render_template("phasefourjobs.html")

#render rocketlabsjobs json
@app.route('/rocketlabsjobs')
def rocketlabsjobs():
    return render_template("rocketlabsjobs.html")

#render bigelowjobs json
@app.route('/bigelowjobs')
def bigelowjobs():
    return render_template("bigelowjobs.html")

#render moonexpressjobs json
@app.route('/moonexpressjobs')
def moonexpressjobs():
    return render_template("moonexpressjobs.html")

#render moonexpressjobs json
@app.route('/planetlabsjobs')
def planetlabsjobs():
    return render_template("planetlabsjobs.html")




@app.route('/test')
def test():
    #next launch
    with urllib.request.urlopen("http://spaceflight.watch/nextlaunch") as url:
        nextlaunch = json.loads(url.read().decode())
    return render_template("test.html",date=nextlaunch[3],time=nextlaunch[0],
        link=nextlaunch[2],next=nextlaunch[1])
