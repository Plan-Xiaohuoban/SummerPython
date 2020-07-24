
GPA = 4.1
name = "Jacky"

info = "Jack's GPA is 4.0, but he still isn't happy"  # 纯字符串
info1 = "%s's GPA is %0.1f, but he still isn't happy " % (name, GPA)  # 百分号格式化
info2 = "{}'s GPA is {}, but he still isn't happy".format(name, GPA)  # format 格式化
info3 = f"{name}'s GPA is {GPA}, but he still isn't happy"  # f-string 格式化



print(info)
print(info1)
print(info2)
print(info3)

