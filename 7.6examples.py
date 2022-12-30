#1
from random import randint
L1=[]
for i in range(50):
    #L1.append(randint(1,100))
    L1=L1+[randint(1,100)]#alternative
print(L1)
print('\n\n')
#2
L2=L1[:]
for i in range(len(L2)):
    L2[i] =L2[i]**2
print(L2)
print('\n\n')
#3
count =0
for item in L1:
    if item>50:
        count=count+1
print('the numbers in L1 greater than 50 is:',count)
print('\n\n')
#4
frequencies =[]
for i in range(1,101):
    frequencies.append(L1.count(i))
print(frequencies)
print('\n\n')
#5
from random import randint
scores=[]
for i in range(10):
    scores=scores+[randint(1,100)]
print(scores)
scores.sort()
print('Two smallest:',scores[0],scores[1])
print('Two largest:',scores[-1],scores[-2])
print('\n\n')
#6
num_right =0

#Question 1
print('What is the capital of Frence?',end=' ')
guess = input()
if guess.lower()=='paris':
    print('Correct!')
    num_right+=1
else:
    print('Woring.The answer is Paris.')
print('You have ',num_right,'out of 1 right')

#Question 2
print('Which  stste has only one neighbor?',end=' ')
guess =input()
if guess.lower()=='maine':
    num_right+=1
else:
    print('Woring.The answer is Maine(大洋洲).')
print('You have ',num_right,'out of 1 right')
print('\n\n')


#another
questions =['What is the capital of Frence?','Which  stste has only one neighbor?']
answers =['Paris','Maine']

num__right =0
for i in range(len(questions)):
    guess =input(questions[i])
    if guess.lower()==answers[i].lower():
        print('Correct')
        num__right=num__right+1
    else:
        print('Woring.The answer is',answers[i])
    print('You have',num__right,'out of',i+1,'right.')


