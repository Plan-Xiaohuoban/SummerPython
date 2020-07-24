
# 列表可以容纳不同类型的对象
b = ["THU", "PKU", 1, 2, [886, 233]]

# # 索引，从零开始，负数=倒数
# print(b[5])
# print(b[-1])

# # 切片，前闭后开
# print(b[0:2])#[0,2)
# print(b[1:4])


# 列表可修改
# 元素赋值
b[2] = "THU"  # 修改列表 b 的第 2 号元素
print(b)

# 切片赋值
b[:2] = ["shiyida", "shierda"]  # 修改列表 b 的前两个元素的切片
print(b)


b.append("Good")  # 在列表 b 的最后增加一个元素
print(b)

b.insert(2, "Bad")  # 在位置 2 处插入 "Bad" 这个元素
print(b)

del b[1]  # 根据编号删除，删除列表 b 的第 1 号元素
print(b)

b.remove("Bad")  # 根据元素删除，删除列表中 "Bad" 这个元素
print(b)

i = b.index("THU")  # 查找指定值第一次出现的索引
print(i)
print(b[i])


# 排序，需保证列表内的元素能够比大小
x = [4, 5, 1, 2, 3, 7, 6]
x.sort()  # 正序排序
print(x)

x.sort(reverse=True)  # 倒序排列
print(x)

