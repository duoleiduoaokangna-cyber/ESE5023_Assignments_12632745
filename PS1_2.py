#第二题（1）
import numpy as np
#建立矩阵M1 M2
M1 = np.random.randint(0, 51, size=(5, 10))
M2 = np.random.randint(0, 51, size=(10, 5))

print("M1:")
print(M1)

print("M2:")
print(M2)

#第二题（2）
def Matrix_multip(M1, M2):
    #设置空变量
    M3 = np.zeros((5, 5), dtype=int)
    #循环
    for i in range(5):
        for j in range(5):
            for k in range(10):
                M3[i, j] = M3[i, j] + M1[i, k] * M2[k, j]
    return M3

print("M1 * M2:")
print(Matrix_multip(M1, M2))
