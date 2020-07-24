score_calculus = 61.5
score_la = 78
score_English = 55

# if score_calculus >= 60:
#     grade = "P"
# else:
#     grade = "F"
# print(grade)

# if score_la >= 60:
#     grade = "P"
# else:
#     grade = "F"
# print(grade)

# if score_English >= 60:
#     grade = "P"
# else:
#     grade = "F"
# print(grade)


# 将语句抽象为函数，无需反复传达详细指令


score = 50


def judge_PF(score):
    if score >= 60:
        grade = "P"
    else:
        grade = "F"
    return grade


x = judge_PF(score=99)

print(x)

# print(judge_PF(78))
# print(judge_PF(score=58))
# print(judge_PF(score=64))



# print(judge_PF(score_calculus))
# print(judge_PF(score_la))
# print(judge_PF(score_English))


# # 循环调用函数
# score_list = [45, 68, 79, 56, 99, 100, 58, 66, 78]
# for score in score_list:
#     print(score, judge_PF(score))


# # 函数调用函数
# def judge_grade(score):

#     if judge_PF(score) == "F":
#         return "F"
#     elif score >= 95:
#         return "A"
#     elif score >= 90:
#         return "A-"
#     elif score >= 85:
#         return "B+"
#     else:
#         return "B"


# score_list = [45, 68, 79, 56, 99, 100, 58, 66, 78]
# for score in score_list:
#     print(score, judge_grade(score))


# # 函数调用函数
# def judge_grade(score):
#     if judge_PF(score) == "F":
#         grade = "F"
#     elif score >= 95:
#         grade = "A"
#     elif score >= 90:
#         grade = "A-"
#     elif score >= 85:
#         grade = "B+"
#     else:
#         grade = "B"
#     return grade  #一个入口，一个出口

# score_list = [45, 68, 79, 56, 99, 100, 58, 66, 78]
# for score in score_list:
#     print(score, judge_grade(score))
