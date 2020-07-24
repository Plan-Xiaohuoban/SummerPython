

# s = ["T", "s", "i", "n", "g", "h", "u", "a"]
# print(s[0])  # 索引
# print(s[1:4])  # 切片
# s[0] = "t"  # 索引赋值
# print(s)

s = "Tsinghua"

# print(s[0])  # 索引
# print(s[1:4])  # 切片
# s[0] = "t"  # 索引赋值
# print(s)

a = "Tsing"
b = "hua"
s = a + b  # 字符串拼接
print(s)

s2 = s.replace("Ts", "tSssss")  # 把字符串 s 中的 "Ts" 替换为 "tSssss"
print(s2)


date = "2020-7-24-3-44"
lst = date.split("-")  # 以 "-" 为分隔符把字符串 date 拆分为列表 s
print(lst)

inter = " + "
s2 = inter.join(lst)  # 以字符串 inter 为分隔符把列表 s 拼成字符串 s2
print(s2)


# 搜索字符串
index = s.find("hua")
print(s[index : index + 3])


# temp = list(s)  # ['T', 's', 'i', 'n', 'g', 'h', 'u', 'a']
# temp[0] = "t"  # ['t', 's', 'i', 'n', 'g', 'h', 'u', 'a']
# s3 = "".join(temp)  # tsinghua
