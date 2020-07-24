

score_list = [90, 92, 88, 87, 89]
credit_list = [3, 4, 3, 3, 4]

# 多个参数的函数
def average_weighted(x_list, w_list):
    average = 0

    # 加权相加
    for i in range(len(x_list)):
        average = average + x_list[i] * w_list[i]

    # 除以总学分
    average = average / sum(w_list)
    return average


# 调用函数
# print("平均分 = ", average_weighted(score_list, credit_list))


# gpa_list = [4.0, 4.0, 3.6, 3.6, 3.6]
# credit_list = [3, 4, 3, 3, 4]
# print("平均绩点 = ", average_weighted(gpa_list, credit_list))

# # 改变参数位置，能运行吗？
# print("平均绩点 = ", average_weighted(credit_list, gpa_list))

# # # 关键字参数：参数的作用清晰，顺序无所谓
# print("平均绩点 = ", average_weighted(w_list=credit_list, x_list=gpa_list))


# 关键字参数：可以指定默认值
def average_weighted(x_list, w_list=[4, 4, 4, 4, 4]):
    average = 0
    for i in range(len(x_list)):
        average = average + x_list[i] * w_list[i]  # 加权相加
    average = average / sum(w_list)  # 除以总学分
    return average


# # 可以仅提供部分参数值，其他的采用默认参数
gpa_list = [4.0, 4.0, 3.6, 3.6, 3.6]
print("平均绩点 = ", average_weighted(x_list=gpa_list))

# # print("平均绩点 = ", average_weighted(gpa_list))
