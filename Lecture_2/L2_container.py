a_str = "Tsinghua University"
b_list = ["T", "s", "i", "n", "g", "h", "u", "a", 110]
c_tuple = (1, 2, 3, "go", "go", "go")
d_dict = {"Top1": "Tsinghua", "Top2": "Peking"}
e_set = {1, 2, 3, "go", "go", "go"}

print(a_str)
print(b_list)
print(c_tuple)
print(d_dict)
print(e_set)


a_str = "Tsinghua University"
print(a_str[1:5])  # sing
print(a_str[:5])  # Tsing
print(a_str[-4:])  # sity

b_list = ["h", "u", "a", 110]
print(b_list[1:2])  # ['u']
print(b_list[:3])  # ['h', 'u', 'a']
print(b_list[-1:])  # [110]

print(b_list[100])