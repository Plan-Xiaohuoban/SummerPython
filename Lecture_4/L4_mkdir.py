

# # 想直接保存到子文件夹下
# # 若没有 Output 目录，会报错
# f = open("Output/summer.txt", "w")
# f.write("I wanna go back to Tsinghua.")
# f.close()



import os


folder_name = "Output"
existance = os.path.exists(folder_name)  # 判断文件/文件夹是否存在
print(existance)

if not existance:  # 若文件夹不存在则创建
    os.mkdir(folder_name)

file_name = os.path.join(folder_name, "summer.txt")  # 合并文件名
print(file_name)

f = open(file_name, "w")
f.write("I wanna go back to Tsinghua.")
f.close()
