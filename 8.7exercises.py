#10
word =input('Enter  a word:')
senWords =['darn','dang','freakin','heck','shit','fuck']
for i in senWords:
    word =word.replace(i,'*'*len(i))
print(word)
