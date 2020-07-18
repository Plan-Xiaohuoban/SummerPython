import requests
from bs4 import BeautifulSoup
import json

url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
for i in range(2):  # 只遍历前两页的歌曲
    params = {
        "ct": "24",
        "qqmusic_ver": "1298",
        "new_json": "1",
        "remoteplace": "txt.yqq.song",
        "searchid": "64221885833364721",
        "t": "0",
        "aggr": "1",
        "cr": "1",
        "catZhida": "1",
        "lossless": "0",
        "flag_qc": "0",
        "p": str(i + 1),
        "n": "10",
        "w": "周杰伦",  # 可变
        "g_tk": "5381",
        "loginUin": "943413047",
        "hostUin": "0",
        "format": "json",
        "inCharset": "utf8",
        "outCharset": "utf-8",
        "notice": "0",
        "platform": "yqq.json",
        "needNewCode": "0",
    }

    res = requests.get(url, params=params)
    
    # 上面get的网址是network中，client_search_cp...中Header中URL的网址，而且是？问号之前的内容，？问号之后是参数params里的内容
    js = res.json()  # 使用json()方法将response对象转换为字典/列表
    list_m = js["data"]["song"]["list"]
    for m in list_m:
        print("歌名：《" + m["name"] + "》")
        print("专辑：《" + m["album"]["title"] + "》")
        print("播放链接：https://y.qq.com/n/yqq/song/" + m["mid"] + ".html\n")

