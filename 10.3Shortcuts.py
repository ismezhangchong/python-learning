#1 Shortcut operators
'''Operations like count=count+1 occur so often that there is a shorthand
for them'''
#count=count+1可以简写为 count+=1
#total=total-5可以简写为total-=5
#prod=prod*2  可以简写为 prod*=2

#2 An assignment shortcut
#Look at the code below.
a=0
b=0
c=0
#A nice shortcut is:
a=b=c=0

#Another assignment shortcut
#假设我们有一个包含三个元素的列表 L，我们想将这些元素分配给变量名
#我们可以这么做
L =['wo','ai','hetong']
x=L[0]
y=L[1]
z=L[2]
print(x,y,z)
print('\n')
#Instead,wecando this
from random import shuffle
shuffle(L)
x,y,z =L
print(x,y,z)
#Similary,we can assign three variables at a time likebelow
x,y,z =1,2,3
#类似于之前，我们可以这样交换变量
x,y,z=y,z,x
print(x,y,z)

#Shortcut with conditions(条件)
'''if a==0 and b==0 and c==0:      和
if 1<a and a>b and b<5:
可以简写成'''
#if a==b==c==0:
#if 1<a<b<5:
