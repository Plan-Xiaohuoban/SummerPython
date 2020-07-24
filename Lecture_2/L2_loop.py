

# x_sequence = [1, 2, 3, 4, 5, 6, 7, 8]
# x_sequence = "Tsinghua University"

# for x in x_sequence:  # 把可迭代对象 x_sequence 中的每个元素代入变量 x，然后执行缩进块的语句
#     print(x)


# b = ["THU", "PKU", 1, 2, [886, 233]]
# for item in b:
#     print(item)


# 从 1 累加到 100，需要手写一个这么长的列表吗？直接生成整数序列
# for i in range(3):  # 生成一个范围为 [0,3) 的整数序列
#     print(i)

# for i in range(2, 100):  # 生成一个范围为 [2,10) 的整数序列
#     print(i)

# for i in range(0, 100, 9):  # 生成一个范围为 [0,100)，每 9 个数取一个数的整数序列
#     print(i)



# sum = 0
# for i in range(101):
#     sum += i
#     print("i = ",i)
# print(sum)  # 4950

# while 循环
# x = 1
# while x < 5:#只要满足 x<5，就会不断循环
#     print(x)
#     x = x + 1  # 可能出现死循环

# 分辨 break 与 continue 的不同
age = 1
while age < 100:
    age += 1
    if age == 35:
        continue
    print(age)



