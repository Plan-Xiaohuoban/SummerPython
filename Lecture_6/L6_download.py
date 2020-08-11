import datetime
import json
import os
import re

import requests
from bs4 import BeautifulSoup


def crawl_pic_urls(json_name):
    """
    爬取每个选手的百度百科图片，并保存
    """
    with open(json_name, "r", encoding="UTF-8") as file:
        json_array = json.loads(file.read())

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }

    for i, star in enumerate(json_array):

        name = star["name"]
        link = star["link"]
        print("\n", i, name, link)

        response = requests.get(link, headers=headers,timeout=5)

        bs = BeautifulSoup(response.text, "lxml")

        try:
            pic_list_url = bs.select(".summary-pic a")[0].get("href")
            pic_list_url = "https://baike.baidu.com" + pic_list_url

            pic_list_response = requests.get(pic_list_url, headers=headers,timeout=5)
            bs = BeautifulSoup(pic_list_response.text, "lxml")
            pic_list_html = bs.select(".pic-list img")

            pic_urls = []
            for pic_html in pic_list_html:
                pic_url = pic_html.get("src")
                pic_urls.append(pic_url)
            
            # 根据图片链接列表pic_urls, 下载所有图片，保存在以name命名的文件夹中
            down_pic(name, pic_urls)
        except Exception as e:
            pass


def down_pic(name, pic_urls, path="results/pictures"):
    """
    根据图片链接列表pic_urls, 下载所有图片，保存在以name命名的文件夹中,
    """
    if not os.path.exists(path):  # 若文件夹不存在则创建
        os.mkdir(path)

    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=5)

            # 合成图片的文件名
            pic_name = name + "_" + str(i + 1) + ".jpg"
            filename = os.path.join(path, pic_name)

            with open(filename, "wb") as f:
                f.write(pic.content)
                print("成功下载第%s张图片: %s" % (str(i + 1), str(pic_url)))

        except Exception as e:
            print("下载第%s张图片时失败: %s" % (str(i + 1), str(pic_url)))
            print(e)
            continue


if __name__ == "__main__":

    # 从每个选手的百度百科页面上爬取图片,并保存
    crawl_pic_urls(json_name="./results/20200811.json")