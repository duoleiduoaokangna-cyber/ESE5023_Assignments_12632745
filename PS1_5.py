#第五题（1）
#引入itertools方便进行排列组合
from itertools import product

def Find_expression(x, show=True):
    count = 0
    #生成组合
    for ops in product(["+", "-", ""], repeat=8):
        expression = "1"
    #组合循环计算
        for i in range(8):
            expression = expression + ops[i] + str(i + 2)
    #计数
        if eval(expression) == x:
            if show:
                print(expression, "=", x)
            count = count + 1

    return count

Find_expression(50)

#第五题（2）
#引入matplotlib.pyplot库
import matplotlib.pyplot as plt
#建立空列表
Total_solutions = []
for i in range(1, 101):
    count = Find_expression(i, show=False)
    Total_solutions.append(count)
#画图
plt.plot(range(1, 101), Total_solutions)
plt.xlabel("Target integer")
plt.ylabel("Number of solutions")
plt.title("Total solutions")
plt.grid(True)
plt.show()

print("Maximum:", max(Total_solutions))
print("Minimum:", min(Total_solutions))
#极值
for i in range(100):
    if Total_solutions[i] == max(Total_solutions):
        print("Maximum at:", i + 1)
    if Total_solutions[i] == min(Total_solutions):
        print("Minimum at:", i + 1)