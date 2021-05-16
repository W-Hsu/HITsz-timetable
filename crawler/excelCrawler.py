# coding=utf-8

from interface import config
from crawler import crawlerSession
from errors import CrawlerError

import json
import misc

# crawler public session
sess = crawlerSession.sess

def getExcelRawData() -> bytes:
    UID = crawlerSession.getUID()
    
    excel_params = {
        "format": "excel",
        "_filename_": "export"
    }

    year = config.Semester.year
    sem  = config.Semester.sem
    # param "reportlets" seems to be a json-like stuff.
    # inelegant, indeed. But I'm too lazy to make a change. ;)
    excel_params["reportlets"] = """%5B%7B%22reportlet%22%3A%22%2Fbyyt%2Fpkgl%2F%E5%AD%A6%E7%94%9F%\
E4%B8%BB%E9%A1%B5%E8%AF%BE%E8%A1%A8%E5%AF%BC%E5%87%BA.cpt%22%2C%22xn%22%3A%22""" + year + """%22%2C\
%22xq%22%3A%22""" + sem + "%22%2C%22dm%22%3A%22" + UID + "%22%7D%5D"

    response = sess.post(config.URLs.excel_export, params=excel_params)
    if response.status_code != 200:
        raise CrawlerError("Get Excel: Server responded error code" + response.status_code + ".")
    elif response.headers["content-type"].find("excel")==-1 and\
         response.headers["content-type"].find("xls")==-1:
        raise CrawlerError("Get Excel: Server not responding excel format.")

    return response.content
