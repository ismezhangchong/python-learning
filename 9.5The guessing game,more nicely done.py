from random import randint
#model1
secret_num =randint(1,100)
num_guesses=0
guess =0

while guess!= secret_num and num_guesses <=4:
    guess =eval(input('Enter your guess(1-100):'))
    num_guesses =num_guesses+1
    if guess< secret_num:
        print('HIGHTER.',5-num_guesses,'guesses left.\n')
    elif guess > secret_num:
        print('LOWER.',5-num_guesses,'guesses left.\n')
    else:
        print('You got it !')
if num_guesses ==5 and guess != secret_num:
    print('You lose.The correct number is',secret_num)
#model2
secret_num =randint(1,100)

for num_guesses in range(5):
    guess =eval(input('Enter your guess(1-100):'))
    if guess< secret_num:
        print('HIGHTER.',5-num_guesses-1,'guesses left.\n')
    elif guess > secret_num:
        print('LOWER.',5-num_guesses-1,'guesses left.\n')
    else:
        print('You got it !')
        break
else:
    print('Your lose.The correct number is',secret_num)
    
        
    
