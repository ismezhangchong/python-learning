#1
for i in range(10):
    num =eval(input('Enter number:'))
    if num<0:
        print('Stopped early')
        break
else:
    print('User entered all ten values')
#2
num=eval(input('Enter anumber:'))
'''第一种'''
i=2
while i<num and num%i!=0:
    i=i+1
if i ==num:
    print('Prime')
else:
    print('Not prime')
'''第二种'''
for i in range(2,num):
    if num%i==0:
        print('Not prime')
        break
else:
    print('Prime')
'''简化版'''
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        print('Not prime')
        break
else:
    print('Prime')
