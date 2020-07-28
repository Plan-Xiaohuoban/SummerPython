def judge_PF(score):
    if score >= 60:
        grade = "P"
    else:
        grade = "F"
    return grade


# 改写为匿名函数（lambda 表达式）
f = lambda score: "P" if score >= 60 else "F"
# print(judge_PF(61.5))
# print(f(58))  # 调用方法基本没有区别


# # f(x) = x ^ 2 + 2 * x + 1
f = lambda x: x ** 2 + 2 * x + 1
print(f(0))
print(f(1))
print(f(2))
