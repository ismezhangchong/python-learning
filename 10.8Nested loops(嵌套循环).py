#二维乘法表
for i in range(1,11):
    for j in range(1,11):
        print('{:3d}'.format(i*j),end=' ')
    print()
#解方程
for x in range(-50,51):
    for y in range(-50,51):
        if 2*x+3*y==4 and x-y==7:
            print(x,y)
print()
#找出勾股数
'''
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            if x**2+y**2==z**2:
                print(x,y,z)
'''
#改进版，删除了4，3，5和6，8，10类
for x in range(1,100):
    for y in range(x,100):
        for z in range(y,100):
            if x**2+y**2==z**2:
                for i in range(2,x):
                    if x%i==0 and y%i==0 and z%i==0:
                        break
                else:
                     print((x,y,z),end=' ')
                
                   
