# coding=utf-8

from interface import config

import time
import misc

def parseLoginParams(username, password):
    config.CrawlerParams.username = username
    config.CrawlerParams.password = password


def parseYearSem(year, sem):
    now = time.localtime(time.time())

    # process semester
    if sem=="autumn" or sem=="fall":
        sem = "1"
    elif sem=="spring":
        sem = "2"
    elif sem=="summer":
        sem = "3"
    else:
        if sem!=None:
            print("Warning: Invalid semester name: " + sem)
        if now.tm_mon < 7:
            sem = "2"  # spring
        elif now.tm_mon < 9:
            sem = "3"  # summer
        else:
            sem = "1"  # autumn/fall
    
    # process year
    if year==None:
        year = now.tm_year

    trueyear = year
    if sem=="1":
        year = str(year) + "-" + str(year+1)
    else:
        year = str(year-1) + "-" + str(year)

    config.Semester.trueyear = trueyear
    config.Semester.year = year
    config.Semester.sem  = sem


def parseOutputTarget(filepath, stdout):
    if stdout==True or filepath==None:
        config.OutputTarget.stdout = True
    else:
        config.OutputTarget.stdout = False
        config.OutputTarget.filePath = filepath
    return
