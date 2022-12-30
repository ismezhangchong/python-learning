#1,2
temp= 0
while temp!=-1000:
    temp=eval(input('Enter a temperature(-1000 to quit):'))
    if temp!=-1000:
              print('in Fahrenheit that is',9/5*temp+32)
    else:
        print('Bye')
        
#3
from random import randint
sec=randint(1,10)
guess =0
while guess!= sec:
    guess =eval(input('Guess the secret number:'))
print('You finally got it!')
#4
i=0
while i<10:
    print(i)
    i=i+1
#5
temp =eval(input('Enter a temperature in Celsius:'))
while temp<-273.15:
    temp=eval(input('Impossible.Enter a valid temperature:'))
print('In Fahrenheit,That is',9/5*temp+32)
#6
i =0
while i<50:
    print(i)
    i=i+2
print('Bye!')
