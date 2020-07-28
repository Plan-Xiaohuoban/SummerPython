import random


print(random.random())  # 生成一个 [0,1] 之间的随机浮点数
print(random.randint(100, 200))  # 生成一个 [a,b] 之间的随机整数


# print(random.uniform(3.3, 4.0))  # 产生 [a,b] 之间的随机浮点数，区间可以不是整数

# # 生成 [a,b] 之间间隔为整数的随机整数
# print(random.randint(0, 10)*100)
# print(random.randrange(0, 1000, 100))

# s= "abcdefghijklmnopqrstuvwxyz"
# print(random.choice(s))  # 从序列中随机选取一个元素

# a = [3.0, 3.3, 3.6, 4.0]  # 将序列a中的元素顺序打乱
# random.shuffle(a)  # 原地修改
# print(a)


# # 多个字符中生成指定数量的随机字符串
# print("".join(random.sample(s, 8)))

