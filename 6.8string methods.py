s ='Hi,call me cute guy.677z'
print(s.count(' '))                 #计算s中有多少个‘’
print(s.index('a'))
'''输入第一个a所在的位置,若没有则会报错
解决方案见下'''
print(s.upper())                    #将s中的每个字母替换为大写
print(s.replace('Hi','Hello'))      #替换s中的Hi为Hello
print(s.lower())                    #将s中的每个字母替换为小写
print(s.isalpha())                  #如果s中每个元素都为字母,输出Tue否则为False
x =input('Enter something:')
if x[0].isalpha():
    print('You start  a string with a letter')
    
if not s.isalpha():
    print('Your string contains a non-letter.')
#如下,index的解决方案
if 'z' in s:

    print(s.index('z'))
    
