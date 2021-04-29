# coding: utf-8

from requests.models import HTTPError
from interface import config
from errors import CrawlerError

import typing
import interface.config as config
import requests
import bs4
import json
import misc

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
def get_text() -> typing.Tuple[str, dict]:
    response = sess.get(config.URLs.login_page)
    if response.status_code != 200:
        raise HTTPError("Error getting login page.")

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

    # TODO
    # In addition to checking status code,
    # We shall check the web-contents to make sure we're successfully logged in.
    if response.status_code != 200:
        print(str(response.status_code))
        raise HTTPError("Login Failed!")
    else:
        print("Login Successful!")


def getExcelRawData() -> bytes:

    response = sess.post(config.URLs.uid_query)
    try:
        j = json.loads(response.text)
        UID = j["ID"]
    except json.JSONDecodeError:
        raise CrawlerError("Get UID from session failed!")
    
    excel_params = {
        "format": "excel",
        "_filename_": "export"
    }

    year, smcount = misc.semester(config.DateTime.startDate)
    # param "reportlets" seems to be a json-like stuff.
    # inelegant, indeed. But I'm too lazy to make a change. ;)
    excel_params["reportlets"] = """%5B%7B%22reportlet%22%3A%22%2Fbyyt%2Fpkgl%2F%E5%AD%A6%E7%94%9F%\
E4%B8%BB%E9%A1%B5%E8%AF%BE%E8%A1%A8%E5%AF%BC%E5%87%BA.cpt%22%2C%22xn%22%3A%22""" + year + """%22%2C\
%22xq%22%3A%22""" + str(smcount) + "%22%2C%22dm%22%3A%22" + UID + "%22%7D%5D"

    response = sess.post(config.URLs.excel_export, params=excel_params)
    if response.status_code != 200:
        raise HTTPError(str(response.status_code))
    else:
        pass

    return response.content
