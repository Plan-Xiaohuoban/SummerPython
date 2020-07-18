
import json
import os
from os import makedirs
from os.path import exists

import requests
import logging
from requests.sessions import Session

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)

# 沟通的艺术
INDEX_URL = "https://thuhole.com/"


COOKIE = r"Cookie: UM_distinctid=173533f52eb158-01b0282febac308-4c302372-144000-173533f52ecb08; _cnzz_CV1279007496=has_token%7Cyes%7C1594829653536%26standalone%7Cno%7C1594829653536%26build_info%7C%25REACT_APP_BUILD_INFO%25%7C0%26cr_version_test%7C%5Bnull%5D%7C1594829654536; CNZZDATA1279007496=257965710-1594826329-%7C1594826329"
LIMIT = 10

RESULTS_DIR = "results"
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def get_count(data):

    count = data.get("data").get("count")
    logging.info(f"There are {count} comments now.")

    return count


def save_all(data, name):

    data_path = f"{RESULTS_DIR}/{name}_all.json"
    json.dump(
        data, open(data_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2
    )


def save_comments(data, name):

    data_path = f"{RESULTS_DIR}/{name}.json"
    data_to_dump = {}

    for page in data:
        page_data = data.get(page)
        userlist = page_data.get("data").get("results")

        for user in userlist:
            name = user.get("user_info").get("name")
            text = user.get("content").get("text")

            if data_to_dump.get(name, 0) == 0:
                data_to_dump[name] = [text]
            elif text not in data_to_dump[name]:
                data_to_dump[name].append(text)

    json.dump(
        data_to_dump,
        open(data_path, "w", encoding="utf-8"),
        ensure_ascii=False,
        indent=2,
    )

    logging.info(f"Comments saved in: {data_path}")
    return data_path


def save_comments_txt(data_path):
    with open(data_path, "rb") as f:
        comments = json.load(f)

    txt_name = data_path.split(".")[0] + ".txt"
    with open(txt_name, "w", encoding="utf-8") as f:
        for (k, v) in comments.items():
            f.write("\n【用户名】" + k + "\n")
            for text in v:
                f.write(text + "\n")

    logging.info(f"Comments of pure txt saved in: {txt_name}")


def scrape_api(url):

    logging.info("scraping %s...", url)

    session = Session()
    session.headers.update(
        {
            "Cookie": COOKIE,
            "user-agent": r"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
        }
    )
    # param = {
    #     "action": "getone",
    #     "pid": "22995",
    #     "PKUHelperAPI":3.0,
    #     "jsapiver":"Stable200712125130-443008",
    #     "user_token":"oyynfhsjvhjq3y345aye2ctcsvnlws7d"
    # }

    try:
        response = requests.get(url,params=param)

        if response.status_code == 200:
            print(response.json())
            return response.json()
        logging.error(
            "get invalid status code %s while scraping %s", response.status_code, url
        )
    except requests.RequestException:
        logging.error("error occurred while scraping %s", url, exc_info=True)


def scrape_index():

    record = 0
    data_all_pages = {}

    url = INDEX_URL.format(limit=LIMIT, offset=0)
    data_all_pages[0] = scrape_api(url)

    pages = get_count(data_all_pages[0]) // LIMIT
    logging.info(f"There are {pages} pages")

    for page in range(1, pages):
        url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
        data_all_pages[page] = scrape_api(url)

    return data_all_pages


if __name__ == "__main__":

    url = r"https://thuhole.com/services/thuhole/api.php"
    scrape_api(url)

    # # Only for debugging usage
    # save_all(data_all_pages)
    # with open("results/all_data.json", "rb") as f:
    #     data_all_pages = json.load(f)

    # BookName = "沟通的艺术"

    # data_path = save_comments(data_all_pages, BookName)
    # save_comments_txt(data_path)
