# coding: utf-8

import datetime
import misc
import typing

#==============================#
# Excel Crawler Configurations #
#==============================#

class URLs:
    login_page_url    = "https://sso.hitsz.edu.cn:7002/cas/login?service=http%3A%2F%2Fjw.hitsz.edu.cn%2Fcas"
    uid_query_url     = "http://jw.hitsz.edu.cn/UserManager/queryxsxx"
    excel_export_url  = "http://jw.hitsz.edu.cn/webroot/decision/view/report"


class CrawlerParams:
    username = None,
    password = None,


#==============================#
# ICS Generator Configurations #
#==============================#

# Monday of the first week
class DateTime:
    start_date = None  # datetime.datetime(2021, 2, 22, 0, 0, 0, 0, tzinfo=misc.UTC(8))
    
    # returns year and semester number
    def semester() -> typing.Tuple(str, int):
        start_date = Datetime.start_date
        start_date = datetime.datetime()

        year = ""
        semester = 0
        if start_date.month < 7:
            semester    = 1
            year        = str(start_date.year) + '-' + str(start_date.year + 1)
        else:
            semester    = 2
            year        = str(start_date.year - 1) + '-' + str(start_date.year)

        return year, semester
