print('How many cats do you have?')
numCat = input()

try:
    if int(numCat) >= 4:
        print('That is a lot of cats')
    else:
        print('That is that many cats')
except ValueError:
    print('You did not enter a number.')
    