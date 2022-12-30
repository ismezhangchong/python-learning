L =['A','B','C']
print(' '.join(L))
print(''.join(L))
print(','.join(L))
print('***'.join(L))
#The join method is in some sense(从某种意义上来说) the opposite of split
#他会takes a list of strings并会把他们连接成一个字符串
#下面是猜字谜 for instance'three,there,ether'
'''This sounds like something we could use shuffle for,
but shuffle only works with lists.
What we need to do is convert our string into a list,use shuffle on it,
and then convert the list back into a string.
To turn a string s into a list, we can use list(s). (See Section 10.1.)
To turn the list back into a string, we will use join.'''#convert:转换
from random import shuffle
word = input('Enter a word:')

letter_list =list(word)
shuffle(letter_list)
anagram =''.join(letter_list)
print(anagram)
