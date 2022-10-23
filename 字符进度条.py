import time as t

scale = 100
for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale-i)
    c = (i/scale)*100
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end = " ")
    t.sleep(0.01)

print("\n","正片开始".center(100,"-"))

scale = 50
print("执行开始".center(scale//2, "-"))
start = t.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = t.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    t.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))