# coding: utf-8

import datetime
import misc

#==============================#
# Excel Crawler Configurations #
#==============================#

domain = "https://sso.hitsz.edu.cn:7002/"
login_page_url = "/cas/login?service=http%3A%2F%2Fjw.hitsz.edu.cn%2Fcas"
uid_query_url = "http://jw.hitsz.edu.cn/UserManager/queryxsxx"

excel_export_url = "http://jw.hitsz.edu.cn/webroot/decision/view/report"
excel_file_path = "./export.xlsx"

login_params = {
    "username": "??????????",
    "password": "!!!!!!!!!!",
    "rememberMe": "on"
}

headers = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

#==============================#
# ICS Generator Configurations #
#==============================#

# Monday of the first week
start_date = datetime.datetime(2021, 2, 22, 0, 0, 0, 0, tzinfo=misc.UTC(8))
