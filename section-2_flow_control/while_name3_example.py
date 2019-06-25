spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
        continue # get back to  while condition
    print('Valor ' + str(spam))
