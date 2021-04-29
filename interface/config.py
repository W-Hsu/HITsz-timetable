# coding=utf-8

import datetime
import misc
import typing

#==============================#
# Excel Crawler Configurations #
#==============================#

class URLs:
    login_domain  = "https://sso.hitsz.edu.cn:7002"
    login_page    = "https://sso.hitsz.edu.cn:7002/cas/login?service=http%3A%2F%2Fjw.hitsz.edu.cn%2Fcas"
    uid_query     = "http://jw.hitsz.edu.cn/UserManager/queryxsxx"
    excel_export  = "http://jw.hitsz.edu.cn/webroot/decision/view/report"


class CrawlerParams:
    username = None
    password = None


#==============================#
# ICS Generator Configurations #
#==============================#

# Monday of the first week
class DateTime:
    startDate = datetime.datetime(1920, 1, 20, tzinfo=misc.UTC(8))


class OutputTarget:
    stdout = True
    filePath = None
    