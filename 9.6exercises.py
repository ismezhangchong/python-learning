#9
import math,random
n =eval(input())
def sqrt_binary(n):
    low, up ,a=0,n,10**(-10)
    while True:
        mid =(low +up )/2
        if abs(mid**2-n)<a:
            return mid
        else:
            if mid**2>n:
                up=mid
            if mid**2<n:
                low =mid
print(sqrt_binary(n))
print(math.sqrt(n))
#19
num=random.sample(range(1,10),9)
cols=random.sample(range(9),9)
rows=random.sample(range(9),9)
square=[[num[(r+c)%9]for c in cols]for r in rows]
for line in square:print(line)
