from flask import Flask, render_template
import datetime, spider

def getnext():
    launches = spider.launches();
    launch_dates = spider.dates();
    launch_times = spider.times();
    #list = []
    next_launch = launches[0]
    next_launch_date = launch_dates[0]
    next_launch_time = launch_times[0]
    link = "https://www.youtube.com/embed/7cjPwT-Nd38"
    #link2 = "https://www.youtube.com/embed/sqlC1Ag0ndQ"
    #link3 = "https://www.youtube.com/embed/t4N5zsDEVuQ"
    file = open("templates/nextlaunch.html","w")
    file.write("{\n")
    file.write("\"" + next_launch_time + "\",\n")
    file.write("\"" + next_launch + "\",\n")
    file.write("\"" + link + "\",\n")
    file.write("\"" + next_launch_date + "\"\n")
    file.write("}")
    file.close()
    #list.append(next_launch_time)
    #list.append(next_launch)
    #list.append(link)
    #list.append(next_launch_date)
    #return list

def upcoming():
    launches = spider.launches();
    launch_dates = spider.dates();
    launch_times = spider.times();
    #list = []
    file = open("templates/upcominglaunches.html","w")
    file.write("{\n")
    file.close()
    for i in range(1,len(launches)):
        next_launch = launches[i]
        next_launch_time = launch_times[i]
        next_launch_date = launch_dates[i]
        #list.append([next_launch_time,next_launch,next_launch_date])
        file = open("templates/upcominglaunches.html","a")
        file.write("[\"" + next_launch + "\",\n")
        file.write("\"" + next_launch_time + "\",\n")
        file.write("\"" + next_launch_date + "\"],\n")
    file = open("templates/upcominglaunches.html","r")
    lines = file.readlines()
    lines[len(lines)-1] = lines[len(lines)-1][:-2]
    file.close()
    file = open("templates/upcominglaunches.html","w")
    file.writelines(lines)
    file.close()
    file = open("templates/upcominglaunches.html","a")
    file.write("}")
    file.close()
    #return list

getnext()
