def fabonaci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fabonaci(n-1)+fabonaci(n-2)

def main():
    汉字命个名试试 = eval(input("请输入对应项数："))
    print(fabonaci(汉字命个名试试))
    return

main()