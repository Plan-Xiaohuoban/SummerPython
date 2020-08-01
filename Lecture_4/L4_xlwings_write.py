

import random

# 若无法导入，则pip install xlwings
import xlwings as xw

"""
开启一个表格应用，注意两个参数。
visible
Ture：可见excel
False：不可见excel

add_book
True:打开excel并且新建工作簿
False：不新建工作簿
"""
app = xw.App(visible=True, add_book=False)


# 打开工作表
wb = app.books.open("社会实践报名表.xlsx")
print(app.books.active)


# 打开工作簿
sht = wb.sheets["sheet1"]


# 读取特定单元格
sht.range("A1")
# sht.range("A1").value


print(sht["A1"].value)

sht["A2"].value = "阿富汗"


countries = [
    "阿富汗",
    "伊拉克",
    "约旦",
    "黎巴嫩",
    "以色列",
    "巴勒斯坦",
    "沙特阿拉伯",
    "巴林",
    "卡塔尔",
    "科威特",
    "阿拉伯联合酋长国",
    "阿曼",
    "也门",
    "格鲁吉亚",
    "亚美尼亚",
    "阿塞拜疆",
    "土耳其",
    "塞浦路斯",
]

# 默认按照行赋值
sht["A2"].value = countries

# 范围赋值
sht["B2:Z2"].value = ""


# 按列赋值
sht["A2"].options(transpose=True).value = countries


# 用随机数填充第二列
description = ["第" + str(random.randint(2, 8)) + "公司" for x in range(20)]
sht["B2"].options(transpose=True).value = description[: len(countries)]

# 随机选几个院系填充第三列
depart_list = ["电子", "自动化", "工物", "土木", "水利", "社科", "航院"]

depart = [depart_list[random.randint(0, len(depart_list)) - 1] for x in range(20)]
sht["C2"].options(transpose=True).value = depart[: len(countries)]


# 随机选几个院系填充第四列
depart = [random.randint(1, 20) for x in range(20)]
sht["D2"].options(transpose=True).value = depart[: len(countries)]


# 第五列
plan = [random.choice(["唱", "跳", "rap", "篮球"]) for x in range(20)]
sht["e2"].options(transpose=True).value = plan[: len(countries)]

# 关闭workbook 和 app
wb.save()
wb.close()
app.quit()
