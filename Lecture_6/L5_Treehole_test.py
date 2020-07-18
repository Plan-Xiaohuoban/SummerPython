
import json
import logging
import os
from os import makedirs
from os.path import exists

import requests
from requests.sessions import Session
from fake_useragent import UserAgent
COOKIE = r"UM_distinctid=173533f52eb158-01b0282febac308-4c302372-144000-173533f52ecb08; _cnzz_CV1279007496=has_token%7Cyes%7C1594829653536%26standalone%7Cno%7C1594829653536%26build_info%7C%25REACT_APP_BUILD_INFO%25%7C0%26cr_version_test%7C%5Bnull%5D%7C1594829654536; CNZZDATA1279007496=257965710-1594826329-%7C1594826329"


def scrape_api(url, params):

    logging.info("scraping %s...", url)
    ua = UserAgent()
    
    # headers = {'User-Agent':ua.random}
    session = Session()
    session.headers.update(
        {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Connection": "keep-alive",
            "Cookie": COOKIE,
            "Host": "thuhole.com",
            "Referer": "https://thuhole.com/",
            "TE": "Trailers",
            "user-agent": r"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
        }
    )

    try:
        response = requests.get(url=url, params=params)
        print(response.status_code)

        if response.status_code == 200:
            return response.json()

        logging.error(
            "get invalid status code %s while scraping %s", response.status_code, url
        )
    except requests.RequestException:
        logging.error("error occurred while scraping %s", url, exc_info=True)


if __name__ == "__main__":

    url = r"https://thuhole.com/services/thuhole/api.php"
    params = {
        "action": "getone",
        "pid": "22995",
        "PKUHelperAPI": 3.0,
        "jsapiver": "Stable200712125130-443008",
        "user_token": "oyynfhsjvhjq3y345aye2ctcsvnlws7d",
    }
    scrape_api(url, params)
