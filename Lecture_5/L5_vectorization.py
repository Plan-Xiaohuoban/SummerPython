import time
import numpy as np
import array

n = 3000
a = array.array("i")
for i in range(n):
    a.append(i)

b = array.array("i")
for i in range(n, 2*n):
    b.append(i)

# 使用普通循环
tic = time.process_time()
outer_product = np.zeros((n, n))

for i in range(len(a)):
    for j in range(len(b)):
        outer_product[i][j] = a[i] * b[j]

toc = time.process_time()

# print("outer_product = " + str(outer_product))
print("Computation time = " + str(1000 * (toc - tic)) + "ms")


# NumPy矢量运算
n_tic = time.process_time()
outer_product = np.outer(a, b)
n_toc = time.process_time()

# print("outer_product = " + str(outer_product))
print("Computation time = " + str(1000 * (n_toc - n_tic)) + "ms")

