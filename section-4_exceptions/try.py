def div52By(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:
        print('Error: you tried to divide by zero')

print(div52By(2))
print(div52By(12))
print(div52By(0))
print(div52By(1))