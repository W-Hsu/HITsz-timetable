# coding=utf-8

import datetime
import misc

#==============================#
# Excel Crawler Configurations #
#==============================#

class URLs:
    login_domain    = "https://sso.hitsz.edu.cn:7002"
    login_page      = "https://sso.hitsz.edu.cn:7002/cas/login?service=http%3A%2F%2Fjw.hitsz.edu.cn%2Fcas"
    uid_query       = "http://jw.hitsz.edu.cn/UserManager/queryxsxx"
    schoolcal_query = "http://jw.hitsz.edu.cn/Xiaoli/queryMonthList"
    exam_query      = "http://jw.hitsz.edu.cn/kscxtj/queryXsksByxhList"
    excel_export    = "http://jw.hitsz.edu.cn/webroot/decision/view/report"


class CrawlerParams:
    username = None
    password = None


#==============================#
# ICS Generator Configurations #
#==============================#

# 
class Semester:
    trueyear = "1920"
    year     = "1920-1921"
    sem      = "1"


class OutputTarget:
    stdout   = True
    filePath = None
    