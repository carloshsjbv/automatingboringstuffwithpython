# This is a guess number game
import random
import sys
from random import randint

print('Hello, what is your name?')
name = input()

secretNumber = randint(1, 10)

print('Hi ' + name + ', I am thinking in a number between 1 and 10. Try to guess it!')

for i in range(1, 7):
    print('Take a guess')

    try:
        number = int(input())
    
        if number > secretNumber:
            print('Not to high...')
        elif number < secretNumber:
            print('Not to low...')
        else:
            print('Congrats, you guessed my number in ' + str(i) + ' guesses')
            sys.exit()
    except ValueError:
        print('You did not type a number')

print('You took could not guess which number I was thinking of. The number was ' + str(secretNumber))