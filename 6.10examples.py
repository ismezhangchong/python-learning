#1
print('\n'*4)
#结果为五个空白行
#2
s = input('Enter some text')
for i in range(len(s)):
    if s[i]=='a':
        print(i)
#3
doubled_s =''
for c in s:#这使用了第6.7二种循环,下面用了6.3的最后一例:'+'的用法
    doubled_s =doubled_s +c*2
    print(doubled_s)
#4
name = input('Enter your name:')
for i in range(len(name)):
    print(name[:i+1],end=' ')
print('\n')
#5
s ="adsDFasdERmp'hhbpbn;fkhk."
s= s.lower()
for c in ',.;:-?()\'"':
    s = s.replace(c,'')
print(s)
#6
s= '3.14159'
print(s[s.index('.'):])
'''a more mathematical way'''
from math import floor
num =3.14159
print(num - floor(num))
#8
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key ='qwertyuiopasdfghjklzxcvbnm'
secret_message = input('Enter your message:')
secret_message = secret_message.lower()

for c in secret_message:
    if c.isalpha():
        print(key[alphabet.index(c)],end='')
    else:
        print(c,end='')
