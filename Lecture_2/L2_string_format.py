
age = 2.3
name = "Jack"
info = "{}'s GPA is {}, but he is happy.".format(name, age)
info2 = " {:-^10s}'s GPA is {:#<10.5f}, but he is happy.".format(name, age)

print(info)
print(info2)