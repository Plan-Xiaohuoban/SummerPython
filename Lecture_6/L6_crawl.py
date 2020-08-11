import datetime
import json
import os
import re

import requests
from bs4 import BeautifulSoup


def crawl_wiki_data():
    """
    爬取百度百科中《乘风破浪的姐姐》中参赛嘉宾的信息，返回html
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    url = "https://baike.baidu.com/item/乘风破浪的姐姐"
    try:
        response = requests.get(url, headers=headers)
        print(response.text)

        # 将一段文档传入BeautifulSoup的构造方法,就能得到一个文档的对象, 可以传入一段字符串
        soup = BeautifulSoup(response.text, "lxml")

        # 返回的是参数 log-set-param 为 table-view 的<table>所有标签
        tables = soup.find_all("table", {"log-set-param": "table_view"})


        crawl_table_title = "参赛嘉宾"
        for table in tables:
            # 对当前节点前面的标签和字符串进行查找
            table_titles = (
                table.find_previous("div").find_previous("div").find_all("h3")
            )
            for title in table_titles:
                if crawl_table_title in title:
                    return table
    except Exception as e:
        print(e)


def parse_wiki_data(table_html, folder_name="results"):
    """
    从百度百科返回的html中解析得到选手信息，以当前日期作为文件名，存JSON文件,保存到work目录下
    """
    bs = BeautifulSoup(str(table_html), "lxml")
    all_tds = bs.find_all("td")
    stars = []

    for item in all_tds[0:]:
        try:
            all_info = item.find_all("a")
            star = {}
            star["name"] = all_info[0].text  # 姓名
            star["link"] = "https://baike.baidu.com" + all_info[0].get(
                "href"
            )  # 个人百度百科链接
            stars.append(star)
        except Exception as e:
            print(e)

    # 生成子文件夹和文件名，保存文件
    if not os.path.exists(folder_name):  # 若文件夹不存在则创建
        os.mkdir(folder_name)

    today = datetime.date.today().strftime("%Y%m%d")
    filename = os.path.join(folder_name, today + ".json")

    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(stars, f, ensure_ascii=False)

    print("信息存储完成！")


if __name__ == "__main__":

    # 爬取百度百科中《乘风破浪的姐姐》中参赛选手信息，返回<class 'bs4.element.Tag'>类型的的html对象
    html = crawl_wiki_data()

    # 把这段html变成字符串并保存，以便查看
    with open("chengfengpolang.html", "w") as f:
        f.write(str(html))

    # 解析html得到选手信息，保存为json文件
    parse_wiki_data(html)

