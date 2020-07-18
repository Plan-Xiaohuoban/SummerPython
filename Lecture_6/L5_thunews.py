

import json
import logging
import os
from os import makedirs
from os.path import exists

import requests
from requests.sessions import Session

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)



def scrape_api(url):

    logging.info("scraping %s...", url)

    try:
        response = requests.get(url=url)
        print(response.status_code)
        print(response.encoding)

        response.encoding = 'utf-8'

        if response.status_code == 200:
            return response.text

        logging.error(
            "get invalid status code %s while scraping %s", response.status_code, url
        )
    except requests.RequestException:
        logging.error("error occurred while scraping %s", url, exc_info=True)


if __name__ == "__main__":

    url = r"https://news.tsinghua.edu.cn/"
    url = r"https://news.tsinghua.edu.cn/info/1014/80115.htm"
    info = scrape_api(url)


    logging.info("Ended")
    print(info)
