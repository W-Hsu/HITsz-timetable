# coding=utf-8

from crawler import crawlerSession
from interface import config
from errors import CrawlerError

import datetime
import json
import copy

# crawler public session
sess = crawlerSession.sess

def getExamDates() -> list:
    exam_list = []

    exam_params = {
        "ppylx": "1",
        "pkkyx": "",
        "pxn": config.Semester.year,
        "pxq": config.Semester.sem,
        "pageNum": "1",
        "pageSize": "4"
    }
    response = sess.post(config.URLs.exam_query, params=exam_params)
    if response.status_code!=200:
        raise CrawlerError("Query Exam: Server responded error code" + str(response.status_code) + ".")
    
    try:
        j = json.loads(response.text.replace("\r\n", ""))
        for i in j["list"]:
            exam_start = datetime.datetime.strptime(i["KSRQ2"], "%m月%d日")
            exam_start = exam_start.replace(year=int(config.Semester.trueyear))

            starthm = i["KSJTSJ"].split("-")[0].split(":")
            endhm   = i["KSJTSJ"].split("-")[1].split(":")
            
            exam_start = exam_start.replace(hour=int(starthm[0]), minute=int(starthm[1]))
            exam_end   = exam_start.replace(hour=int(endhm[0]), minute=int(endhm[1]))

            exam_list.append({
                "examname": i["KCMC"],
                "classroom": i["CDDM"],
                "start": exam_start,
                "end": exam_end
            })
    except json.JSONDecodeError:
        raise CrawlerError("Query Exam: Get exam json from session failed.")
    except KeyError:
        raise CrawlerError("Query Exam: Cannot find critical info in requested exam json.")

    return exam_list
