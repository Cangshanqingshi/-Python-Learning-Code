import turtle as t1
import time as t2

# 线间留白
def drawgap():
    t1.penup()
    t1.fd(5)
    return

#  绘制单线段
def drawline(draw):
    drawgap()
    t1.pendown() if draw else t1.penup()
    t1.fd(40)
    drawgap()
    t1.right(90)  # 下一步方向选最多的，其他的再调就可以了
    return

#  绘制一个七段数码管
def drawdigit (digit):
    drawline(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 6, 8] else drawline(False)
    t1.left(90)  #  转90度扳直方向
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 7,  8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    # 为下一次绘制做准备
    t1.left(180)
    t1.penup()
    t1.fd(20)
    return

#  解析时间字符串并绘制, date为日期，格式为'%Y-%m=%d+'
def drawdate(date):
    t1.pencolor("red")
    for i in date:
        if i == '-':
            t1.write('年', font = ("Arial", 18, "normal"))
            t1.pencolor("green")
            t1.fd(40)
        elif i == '=':
            t1.write('月', font=("Arial", 18, "normal"))
            t1.pencolor("blue")
            t1.fd(40)
        elif i == '+':
            t1.write('日', font=("Arial", 18, "normal"))
            t1.pencolor("orange")
            t1.fd(40)
        elif i == '*':
            t1.write('时', font=("Arial", 18, "normal"))
            t1.pencolor("brown")
            t1.fd(40)
        elif i == '/':
            t1.write('分', font=("Arial", 18, "normal"))
            t1.pencolor("pink")
            t1.fd(40)
        elif i == '|':
            t1.write('秒', font=("Arial", 18, "normal"))
        else:
            drawdigit(eval(i))
    return

# 绘制整个时间的七段数码管
def main():
    t1.setup(1600, 350, 200, 200)
    t1.penup()
    t1.fd(-600)
    t1.pensize(5)
    drawdate(t2.strftime('%Y-%m=%d+%I*%M/%S|', t2.gmtime()))
    t1.hideturtle()  # 隐藏箭头
    t1.done()  # 留下画布
    return

main()