import math

scores = [40, 50, 60, 70, 80, 90]  # 班级成绩，如何统一调分？

# 全班加五分
new_scores = []  # 新建空列表
for x in scores:  # for 循环，把列表 scores 中的每个元素代入变量 x，然后执行缩进块的语句
    new_scores.append(x + 5)  # 每人增加五分
print(new_scores)

new_scores = [x + 5 for x in scores]  # 列表生成式，一句搞定
print(new_scores)

new_scores = [math.sqrt(x) * 10 for x in scores]  # 开根号乘十
print(new_scores)

# 列表生成式 + 条件判断
new_scores = [x for x in scores if x >= 60]  # 获取及格的同学
print(new_scores)

new_scores = [61 for x in scores if x < 60]  # 捞起不及格的同学
print(new_scores)

new_scores = [x + 20 if x + 20 <= 100 else 100 for x in scores]  # 全班加20分，超过100的变成100
print(new_scores)


# # 用range()和列表生成式制造列表
# numbers = [x * 10 for x in range(4, 10)]
# print(numbers)
