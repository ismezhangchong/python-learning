#1
for i in range(10):
    num =eval(input('Entr number:'))
    if num<0 or num ==0:
        break
print('\n')
'''also can be accomplished with a while loop'''
i =0
num=1
while i<10 and num>0:
    num=eval(input('Enter a number:'))#'''
#2
temp =0
while temp!=-1000:
    temp=eval(input(';'))
    if temp!=-1000:
        print(9/5*temp+32)
    else:
        print('Bye')
#'''
while True:
    temp=eval(input(':'))
    if temp==-1000:
        print('Bye')
        break
    print(9/5*temp+32)#'''
