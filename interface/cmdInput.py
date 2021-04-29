# coding: utf-8

from interface import config

def parse(username, password, filepath, stdout):
    config.CrawlerParams.username = username
    config.CrawlerParams.password = password

    if stdout==True or filepath==None:
        config.OutputTarget.stdout = True
    else:
        config.OutputTarget.stdout = False
        config.OutputTarget.filePath = filepath
    
    return
