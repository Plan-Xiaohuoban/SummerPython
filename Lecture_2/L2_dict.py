

names = {"Alex": 2020010483, "Jack": 2019880789, "Tim": [2015050888, "Phd"]}

# print(names["Eva"])  # 通过键访问值
# print(names["Tim"])  # 通过键访问值
# print(names[1])  # 不可通过编号索引（实际上这等于访问不存在的键）

# print("-" * 50)

# 常用字典操作：增删查改
names["Eva"] = [2016050999, "Master"]  # 将新的值关联到键 "Eva" 上（新增键值对）
print(names)
print(names["Eva"])  # 现在可以访问键 "Eva" 了

del names["Jack"]  # 删除键为 "Jack" 的键值对
print(names)

search = "Alex" in names  # 检查字典 names 是否包含键为 "Alex" 的键
print(search)
print("Jimmy" in names)  # 检查字典 names 是否包含键为 "Jimmy" 的键

names["Eva"] = [2020010001, "Professor"]  # 将新的值关联到键 "Eva" 上（覆盖原来的值）
print(names)


# {"Alex": 2020010483, "Jack": 2019880789}