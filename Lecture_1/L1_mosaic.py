import numpy as np
import matplotlib.pyplot as plt

python = plt.imread("./cat.jpg")

python_2 = python[::20, ::20]  # 每隔20个像素取一个像素
plt.imshow(python_2)

plt.savefig("cat_mosiac.jpg")
