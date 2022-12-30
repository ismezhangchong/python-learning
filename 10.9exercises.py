L=[i*3 for i in range(34)]
L.remove(0)
print(L)
#28
'''
5 a b
c 6 2
3 8 d
'''
for a in range(20):
    for b in range(20):
        for c in range(20):
            for d in range(20):
                if 5+a+b==c+6+2==3+8+d==5+c+3==a+6+8\
                   ==b+2+d==5+6+d==b+6+3:
                    print(a,b,c,d)
                
