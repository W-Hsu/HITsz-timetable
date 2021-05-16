# coding=utf-8

import datetime
from interface import config
from crawler import crawlerSession
from errors import CrawlerError

import json

# crawler public session
sess = crawlerSession.sess

def getSchoolCal() -> datetime.datetime:
    startMonday = datetime.datetime

    schoolcal_param = {
        'dm': '',
        'zyw': 'zh',
        'xnxq': '',
        'pxn': config.Semester.year,
        'pxq': config.Semester.sem,
    }

    response = sess.post(config.URLs.schoolcal_query, params=schoolcal_param)
    if response.status_code != 200:
        raise CrawlerError("Get School Calendar: Server responded error code" + response.status_code + ".")
    
    try:
        j = json.loads(response.text.replace("\r\n", ""))
        startMonday_raw = j["xlList"][7]["MON"]
        startMonday = datetime.datetime.strptime(startMonday_raw, "%Y-%m-%d")
    except json.JSONDecodeError:
        raise CrawlerError("Get School Calendar: Get school calendar json from session failed.")
    except KeyError:
        raise CrawlerError("Get School Calendar: Cannot find requested calendar info in json.")
    except ValueError:
        raise CrawlerError("Get School Calendar: Ill-formed date format in requested json")

    return startMonday
