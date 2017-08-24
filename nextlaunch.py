from flask import Flask, render_template
import datetime, spider

def getnext():
    launches = spider.launches();
    launch_dates = spider.dates();
    launch_times = spider.times();
    launch_sites = spider.sites();
    list = []
    next_launch = launches[1]
    next_launch_date = launch_dates[1]
    next_launch_time = launch_times[1]
    next_launch_site = launch_sites[1]
    link = "https://www.youtube.com/embed/sqlC1Ag0ndQ?autoplay=1"
    #link2 = "https://www.youtube.com/embed/t4N5zsDEVuQ"
    file = open("templates/nextlaunch.html","w")
    file.write("{\n")
    file.write("\"time\":\"" + next_launch_time + "\",\n")
    file.write("\"next\":\"" + next_launch + "\",\n")
    file.write("\"link\":\"" + link + "\",\n")
    file.write("\"date\":\"" + next_launch_date + "\",\n")
    file.write("\"site\":\"" + next_launch_site + "\"\n")
    file.write("}")
    file.close()
    list.append(next_launch_time)
    list.append(next_launch)
    list.append(link)
    list.append(next_launch_date)
    list.append(next_launch_site)
    print(list)

def upcoming():
    launches = spider.launches();
    launch_dates = spider.dates();
    launch_times = spider.times();
    launch_sites = spider.sites();
    #list = []
    file = open("templates/upcominglaunches.html","w")
    file.write("[\n")
    file.close()
    for i in range(0,len(launches)):
        next_launch = launches[i]
        next_launch_time = launch_times[i]
        next_launch_date = launch_dates[i]
        next_launch_site = launch_sites[i]
        #list.append([next_launch_time,next_launch,next_launch_date,next_launch_site])
        file = open("templates/upcominglaunches.html","a")
        file.write("[\"" + next_launch_time + "\",\n")
        file.write("\"" + next_launch + "\",\n")
        file.write("\"" + next_launch_date + "\",\n")
        file.write("\"" + next_launch_site + "\"],\n")
    file = open("templates/upcominglaunches.html","r")
    lines = file.readlines()
    lines[len(lines)-1] = lines[len(lines)-1][:-2]
    file.close()
    file = open("templates/upcominglaunches.html","w")
    file.writelines(lines)
    file.close()
    file = open("templates/upcominglaunches.html","a")
    file.write("]")
    file.close()
    #print(list)
    #return list

#getnext()
upcoming()
