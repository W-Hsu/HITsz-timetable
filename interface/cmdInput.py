# coding: utf-8

from interface import config

import datetime
import misc

def parseLoginParams(username, password):
    config.CrawlerParams.username = username
    config.CrawlerParams.password = password


def parseStartDate(y, m, d):
    config.DateTime.startDate = datetime.datetime(int(y), int(m), int(d), 0, 0, 0, tzinfo=misc.UTC(8))


def parseOutputTarget(filepath, stdout):
    if stdout==True or filepath==None:
        config.OutputTarget.stdout = True
    else:
        config.OutputTarget.stdout = False
        config.OutputTarget.filePath = filepath
    return
