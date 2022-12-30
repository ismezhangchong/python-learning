s ='Hi! This is a test.'
print(s.split())
print('\n')
from string import punctuation
#punctuation is a variable countains common punctuation(标点符号)'''
for c in punctuation:
    s = s.replace(c,'')
print(s.split())
s =s.lower()
L =s.split()#数一个单词出现了几次的program
word = input('Enter a word:')
print(word,'appears',L.count(word),'times')
print('\n')
s= '1-800-271-8281'
print(s.split('-'))#除了space,split还可以中断其它的字符串

