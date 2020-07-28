
# 三种常见的 import 方法
import L3_inherit  # 直接导入
import cats.L3_pillow_filters
# import L3_inherit as cc  # 导入并且起一个别名
# from L3_inherit import Hanxin,Libai # 选择性导入一部分

# # 非常不建议的写法
from L3_inherit import *  # 导入模块中的全部

a= Hanxin("韩信", 15)
a.StealTower()

# a = Hanxin("韩信", 15)
# a.StealTower()

b = Libai("Libai")
b.use_skill(2)
