import turtle as t1
import math as m


def koch(size, n):
    if n == 0:
        t1.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            t1.left(angle)
            koch(size/3, n-1)


def main():
    a = eval(input("输入长度(600以内整数,稍微大一些）:"))
    b = eval(input("阶数(整数，小于6会稍微快一点):"))
    topwindow = t1.Screen().getcanvas().winfo_toplevel()
    topwindow.call('wm', 'attributes', '.', '-topmost', '1')
    t1.setup(a + 200, a + 200)
    t1.penup()
    t1.goto(-a/2, m.sqrt(3)/6*a)
    t1.pendown()
    t1.pensize(1)
    t1.speed(10)
    t1.delay(0)
    for i in range(3):
        koch(a, b)
        t1.right(120)
    t1.hideturtle()
    t1.done()


try:
    main()
except:
    print("请正常输入！并且不要在作图期间关闭画布！")
