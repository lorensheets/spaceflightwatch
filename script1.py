from flask import Flask, render_template
import nextlaunch, urllib.request, json, ssl

app=Flask(__name__)

@app.route('/')
def home():

    launch = nextlaunch.getnext()
    upcoming = nextlaunch.upcoming()

    return render_template("index.html", time=launch[0],
    next=launch[1], link=launch[2], date=launch[3], upcoming=upcoming)




if __name__=="__main__":
    app.run(debug=True)

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
