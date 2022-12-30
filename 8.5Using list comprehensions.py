#1Write a program that generates a list L of 50 random numbers between 1 and 100
from random import randint
L =[randint(1,100) for i in range(50)]
print(L)
#2#3
L1=[i**2 for i in L]
print(L1,len([i for i in L if i>50]))
#4
frequenices = [L.count(i) for i in range(1,100)]
print(frequenices)
#Another example
'''The join method can often
be used with list comprehensions
to quickly build up a string.
Here we create a string that contains a random assortment of 1000 letters.'''
from random import choice
alphabet ='qwertyuiopasdfghjklzxcvbnm'
s =''.join([choice(alphabet) for  i in range(1000)])
print(s)
print('\n')
#One more example
'''Suppose we have a list whose elements are lists of size 2, like below:'''
L =[[1,2],[3,4],[5,6]]
'''If we want to flip the order of the entries in the lists,
we can use the following list comprehension'''
M =[[y,x] for x,y in L]
print(M)

#Note
'''You can certainly get away without using list comprehensions,
but once you get the hang of them,
you’ll find they are both quicker to write and easier to read
than the longer ways of creating lists.'''
