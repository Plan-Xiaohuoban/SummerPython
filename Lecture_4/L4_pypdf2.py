# pip install PyPDF2
import PyPDF2

# 创建一个 PdfFileReader 对象
merger = PyPDF2.PdfFileMerger()

# 打开文件
input1 = open("Data_samples\程序员健康指南.pdf", "rb")

# 获取范围内的页数，增加到 merger 中
merger.append(fileobj=input1, pages=(72, 84))  # 73页-84页
merger.append(fileobj=input1, pages=(104, 119))  # 105页-119页


# 输出到文件中
output = open("Output/Chapter_5_7.pdf", "wb")
merger.write(output)

