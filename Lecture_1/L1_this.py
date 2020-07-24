import cmath

a = float(input("输入 a: "))
b = float(input("输入 b: "))
c = float(input("输入 c: "))

# 计算
d = (b ** 2) - (4 * a * c)

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print("结果为 {0} 和 {1}".format(sol1, sol2))

