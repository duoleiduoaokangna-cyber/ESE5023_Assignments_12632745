#第一题
def Print_values(a, b, c):
    if a > b:
        if b > c:
            print(a, b, c)
        else:
            if a > c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if c > b:
            print(c, b, a)
        elif a > c:
            print(b, a, c)
        else:
            print(b, c, a)
#检验程序
print("判断大小")

a = float(input("请输入 a："))
b = float(input("请输入 b："))
c = float(input("请输入 c："))
Print_values(a, b, c)