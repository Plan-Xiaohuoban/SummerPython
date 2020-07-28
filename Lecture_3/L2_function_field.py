def change_GPA(x, target):
    x = target
    print("x = ", x)


linear_algebra = 2.3
print("修改之前的成绩 =", linear_algebra)
change_GPA(linear_algebra, 4.0)
print("修改之后的成绩 =", linear_algebra)  # 修改失败


print("-" * 30)


def change_GPA_list(x_list, target):
    for i in range(len(x_list)):
        GPA_list[i] = target
    print("x_list=", x_list)

GPA_list = [2.0, 2.3, 3.3, 3.6, 1.7]
print("修改之前的成绩列表=", GPA_list)
change_GPA_list(GPA_list, 4.0)
print("修改之后的成绩列表=", GPA_list)

