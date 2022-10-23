import random as r
import time as t
import math as m

start = t.perf_counter()
num = 1000000
n = round(m.log(num, 10))  # 用round函数处理小数尾数
r.seed(10)
num1 = 0
for i in range(num):
    x = r.random()
    y = r.random()
    # 另外可以如此两个一并赋值了：x, y = random(), random()
    if x**2 + y**2 < 1:
        num1 += 1
pi = num1/num*4
end = t.perf_counter()
print("the value of pi is {}".format(pi).center(35, "="))
print("the run-time is {}s".format(end - start).center(35, "="))
print("本次随机的次数为10的{}次方".format(n).center(35, "="))
