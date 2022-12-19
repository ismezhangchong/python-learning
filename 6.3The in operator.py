string =input('Enter something:')
if 'a' in string:
    print('Your string contains the letter a.')
if ';' not in string:
    print('Your string does not contain any semicolons.')
#一个更轻松的用法6.2
x =input('Enter a letter:')
if x in 'aeiou':
    print('x是元音字母')
else:
    print('x是不元音字母')
    
