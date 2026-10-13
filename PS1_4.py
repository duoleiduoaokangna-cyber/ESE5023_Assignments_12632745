#第四题
def Least_moves(x):
    moves = 0
    #判断步数为奇数偶数
    for i in range(x):
        if x == 1:
            break

        if x % 2 == 0:
            x = x // 2
        else:
            x = x - 1

        moves = moves + 1

    print(moves)
Least_moves(2)
Least_moves(5)
#设置X的范围
import random
x = random.randint(1, 100)  
print(" x：", x)
Least_moves(x)
