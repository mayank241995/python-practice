import random

n=random.randint(1,10)
guess=0

while guess!=n:
    guess=int(input('enter the number'))
    if guess > n:
        print('it is greater')
    elif guess <n:
        print('it is lesser')
    else:
        print('you got it',n)