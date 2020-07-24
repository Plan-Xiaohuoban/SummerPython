def recursion():
    print("recursion")
    return recursion()  # 调用自己，且没有退出机制


recursion()  # 无穷递归，必然出错：栈溢出


# def accumulate(n):
#     if n == 1:
#         return 1  # 最小问题，满足这个条件时函数直接返回一个值，退出递归
#     else:
#         return accumulate(n - 1) + n  # 依次加上从 n 递减到 2 的每个数字


# print(f"sum = {accumulate(100)}")
