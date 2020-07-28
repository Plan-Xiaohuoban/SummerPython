import random
import easygui

# easygui.msgbox(msg="Hello world!")


num = easygui.enterbox(
    msg="请输入班级总人数", title="请输入总人数", default=30, strip=True, image=None, root=None
)
print(num)


message = "点名啦！\n\n幸运观众是：" + str(random.randint(1, int(num))) + "号"
# easygui.msgbox(msg=message, title="随机点名", ok_button="OK", image=None, root=None)


# 带图片
# easygui.msgbox(msg=message, title="随机点名", ok_button="OK", image="lottery.jpg", root=None)


# 自选图片
path = easygui.fileopenbox(msg="请选择一张图片", title="选择图片", default="*.jpg")

print(path)
easygui.msgbox(msg=message, title="随机点名", ok_button="OK", image=path, root=None)

