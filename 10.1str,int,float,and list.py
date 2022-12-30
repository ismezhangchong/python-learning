#The built-in function str is used to convert things into strings
print(str(37),str(3.14),str([1,2,3]),str(4/2))


#The int function converts something into an integer.
#The float function converts something into a floating point number.
print(int('37'),float('3.14'),int(3.14))
'''To convert a float to an integer,
the int function drops everything after the decimal point'''

'''The list function takes something
that can be converted into a list and makes into a list.
Here are two uses of it.'''
print(list(range(5)),list('abc'))

#1
for i in range(1,10001):
    s=str(i)
    if s==s[::-1]:
        print(s)
'''We use the str function here
to turn the integer i into a string
so we can use slices to reverse it'''
#2
birthday ='October 15,2004'
year =int(birthday[-4:])
print('You are',2023-year,'years old.')
#3
num =17
digit =str(num)
answer =int(digit[0]) +int(digit[1])
print(answer)
'''+++'''
num =eval(input())
digit =str(num)
answer =0
for i in range(len(digit)):
    answer=answer +int(digit[i])
print(answer)
'''+'''

answer=sum([int(c) for c in str(num)])
print(answer)
#4
num=eval(input())
ipart =int(num)
dpart =num-int(num)
print(ipart,dpart)
#5
print('请打开9.4的简化部分')
