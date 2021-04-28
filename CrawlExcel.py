# coding: utf-8

from requests.cookies import RequestsCookieJar
from requests.models import HTTPError

import config
import typing
import requests
import bs4
import json


# Initialize a requests.Session with a header sqecified with config.header
sess = requests.Session()


# GET login page
# 
# returns:
# - URL of form action page
# - ALL website default input key-values
def get_text() -> str, dict:
    sess.headers.update({
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    })
    response = sess.get(config.login_page_url)
    
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
    # Override allLoginParams with values specified in config.login_params
    for kv in config.login_params.items():
        allLoginParams[kv[0]] = kv[1];

    # Request a page
    response = sess.post(config.domain+loginFormPage, params=allLoginParams)

    if response.status_code != 200:
        print(str(response.status_code))
        raise HTTPError("Login Failed!")
    else:
        print("Login Successful!")


def getUID() -> str:
    response = sess.post(config.uid_query_url)
    print(response.text)
    j = json.loads(response.text)
    return j["ID"]


def getExcelDate(UID) -> bytes:
    excel_params = {
        "format": "excel",
        "_filename_": "export"
    }
    # YES. I think that's ugly too. But I'm lazy ;)
    excel_params["reportlets"] = """%5B%7B%22reportlet%22%3A%22%2Fbyyt%2Fpkgl%2F%E5%AD%A6%E7%94%9F%\
E4%B8%BB%E9%A1%B5%E8%AF%BE%E8%A1%A8%E5%AF%BC%E5%87%BA.cpt%22%2C%22xn%22%3A%222020-2021%22%2C%22xq%2\
2%3A%22 2 %22%2C%22dm%22%3A%22""" + UID + "%22%7D%5D"

    response = sess.post(config.excel_export_url, params=excel_params)
    if response.status_code != 200:
        raise HTTPError(str(response.status_code))
    else:
        pass

    with open(config.excel_file_path, 'wb') as fp:
        for chunk in response.iter_content(chunk_size=4096):
            if chunk:
                fp.write(chunk)
