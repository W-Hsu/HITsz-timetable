# coding=utf-8

from errors import CrawlerError
from interface import config

import requests
import typing
import bs4
import json

# Initialize a requests.Session with a fake header
sess = requests.Session()
sess.headers.update({
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
})


# GET login page, in order to:
# - generates all input param of the login form
# - get the login form action page
# 
# returns:
# - URL of form action page
# - ALL website default input key-values
def get_login_page() -> typing.Tuple[str, dict]:
    response = sess.get(config.URLs.login_page)
    if response.status_code != 200:
        raise CrawlerError("Get Login Page: Server responded error code" + str(response.status_code) + ".")

    pageSoup = bs4.BeautifulSoup(response.text, "html.parser")
    formSoup = pageSoup.find("form")

    # Get form's attribute "action", which means action page
    form_page = formSoup.get("action")

    # Get all form input key and default values
    default_values = dict()
    inputSoups = formSoup.find_all("input")
    for i in inputSoups:
        default_values[i.get("name")] = i.get("value")

    return form_page, default_values


# log in jw system
def login(loginFormPage, allLoginParams):
    # Add the given username and password into login params.
    allLoginParams["username"] = config.CrawlerParams.username
    allLoginParams["password"] = config.CrawlerParams.password

    # Login!
    # Get a validated COOKIE for our session.
    response = sess.post(config.URLs.login_domain + loginFormPage, params=allLoginParams)

    if response.status_code != 200:
        raise CrawlerError("Login: Server responded error code: " + str(response.status_code) + ".")
    elif response.text.find("账号密码验证失败")!=-1:
        raise CrawlerError("Login: Incorrect username or password.")


# query internal uid
def getUID() -> str:
    response = sess.post(config.URLs.uid_query)
    UID = ""

    if response.status_code!=200:
        raise CrawlerError("Query User UID: Server responded error code" + str(response.status_code) + ".")
    try:
        j = json.loads(response.text.replace("\r\n", ""))
        UID = j["ID"]
    except json.JSONDecodeError:
        raise CrawlerError("Query User UID: Get userinfo json from session failed.")
    except KeyError:
        raise CrawlerError("Query User UID: Cannot find id in requested userinfo json.")

    return UID
