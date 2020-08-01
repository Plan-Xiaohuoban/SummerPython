import locale
import time

locale.setlocale(locale.LC_CTYPE, "chinese")
date = time.strftime("%Y年%m月%d日")

univ = "华清大学"
target = "利比亚"
description = "华人餐馆"
department = "画画学院"
prof = "张小明"
number = 3
plan = "画画"
sender = target + description + "有限公司"

title = f"关于邀请{univ}师生赴{target}进行暑期社会实践的函"
receiver = f"共青团{univ}委员会："
text = f"获悉{univ}正在组织优秀学生利用暑假赴海外国家进行社会实践的活动，\
作为在{target}的{description}，我们诚挚的邀请以{univ}{department}{prof}教授带队\
的师生代表团共计{number}人来{target}进行社会实践，{plan}。"

if __name__ == "__main__":
    print(title)
    print(receiver)
    print(text)
    print(sender)
    print(date)
