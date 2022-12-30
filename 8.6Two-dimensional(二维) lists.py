L=[[1,2,3],[4,5,6],[7,8,9]]
for r in range(3):
    for c in range(3):
        print(L[r][c],end='')
    print()
    
L=[[0]*5]*10
for r in range(1,7):
    for c in range(4):
        print(L[r][c],end='')
    print()
print(L)
print([[r for r in range(5)]for c in range(10)])
print('\n')
count = 0
for r in range(10):
    for c in range(5):
        if L[r][c]%2==0:
            count =count+1
from pprint import pprint
print([[r for r in range(5)]for c in range(10)])
L=[[r for r in range(3)] for c in range(5)]
pprint(L)
print('\n')
#count =sum([1 for r in range(10) for c in range(5) if l[r][c]%2==0])
L=[[0]*50 for i in range(100)]
print(L)
print([[[0]*5 for i in range(5)] for j in range(5)])
#未完成'''
