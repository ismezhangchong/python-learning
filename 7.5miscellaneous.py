L=['j','i','a','y','o','s','h','u','a','i']
M=L[:]
#M=L
L[0]=9

#making copy of lists
print(L,M,sep='\n')
#changing lists
L[1]=9
print(L)
L.insert(7,9)
print(L)
del L[1]
print(L)
del L[:2]
print(L)
