
# 三种常见的 import 方法
import L3_inherit  # 直接导入

import cats.L3_pillow_filters as cf

import sys
sys.path.append("../")
import Lecture_2.L2_list_comprehension as L2

print(L2.scores)
# import L3_inherit as cc  # 导入并且起一个别名
# from L3_inherit import Hanxin,Libai # 选择性导入一部分

# # 非常不建议的写法

