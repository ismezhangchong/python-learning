L =[i for i in range(5)]
#这方法像数学里的集合表示法一样
string ='Hello'
L =[1,14,5,9,12]
M =['一'*3,'二'*3,'三'*3,'四'*3,'五'*3,'六'*3]
print(M)
#看下面！
L1 =[0 for i in range(10)]
print(L1)
L2 =[i**2 for i in range(1,8)]
print(L2)
L3 =[i*10 for i in L]
print(L3)
L4 =[c*2 for c in string]
print(L4)
L6 =[m[0] for m in M]
print(L6)
L7 =[i for i in L if i<10]
print(L7)
L8 =[m[0] for m in M if len(m)==3]
print(L8)
X=[]#对比一下L8和print(X)
for m in M:
    if len(m)==3:
        X.append(m[0])
print(X)
print('\n'*3)
#multiple fors
L =[[i,j] for i in range(2) for j in range(2)]
print(L)
'''下面一项和此处相同'''
L =[]
for i in range(2):
    for j in  range(2):
        L.append([i,j])
print(L)
print('\n')

#Here is another example
print([[i,j] for i in range(4) for j in range(i)])

