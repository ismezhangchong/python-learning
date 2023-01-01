from random import randint
a=eval(input('Enter a num in[1,4]'))
b=eval(input('Enter a num in[1,4]'))
c=eval(input('Enter a num in[1,4]'))
d=eval(input('Enter a num in[1,4]'))
print('Your num is:',a,b,c,d)

while not a==b==c==d:
    x=randint(1,4)
    if x==1:
        a,b,c=(a+1)%4,(b+1)%4,(c+1)%4
        print(a,b,c,d)
    if x==2:
        a,b,d=(a+1)%4,(b+1)%4,(d+1)%4
        print(a,b,c,d)
    if x==3:
        a,c,d=(a+1)%4,(c+1)%4,(d+1)%4
        print(a,b,c,d)
    if x==4:
        b,c,d=(b+1)%4,(c+1)%4,(d+1)%4
        print(a,b,c,d)
       
    
