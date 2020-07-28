def show():
    pass


s = "tsinghua"
b = 124
print(type(s))  # 字符串是 str 类的对象
print(type(b))  # 数字是 int 类的对象
print(type(show))  # 自定义函数是 function 类的对象
print(type(print))  # print函数是 builtin_function_or_method 类的对象

print("-" * 30)


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)  # value
print(type(a))  # type
print(id(a))  # identity


print("-" * 30)

b = [1, 2, 3, 4, 5, 6, 7, 8]
print(b)  # value
print(type(b))  # type
print(id(b))  # identity

# print("-" * 30)

# # 两个列表是否相等？是否是同一个对象？
print(a == b)
print(a is b)

