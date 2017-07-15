from flask import Flask, render_template
import datetime, spider

def getnext():
    launches = spider.launches();
    launch_dates = spider.dates();
    launch_times = spider.times();
    list = []
    #time = datetime.datetime(2017, 6, 23, 10, 10, 0).timestamp()
    next_launch = launches[1]
    next_launch_date = launch_dates[1]
    next_launch_time = launch_times[1]
    link = "https://www.youtube.com/embed/7cjPwT-Nd38"
    list.append(next_launch_time)
    list.append(next_launch)
    list.append(link)
    list.append(next_launch_date)
    return list

def upcoming():
    launches = spider.launches();
    launch_dates = spider.dates();
    launch_times = spider.times();
    list = []
    for i in range(2,len(launches)):
        next_launch = launches[i]
        next_launch_time = launch_times[i]
        next_launch_date = launch_dates[i]
        list.append([next_launch_time,next_launch,next_launch_date])
    return list
