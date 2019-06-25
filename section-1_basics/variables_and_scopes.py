myVar = 42 # global variable

def eggs(): 
    myVar = 43 # local variable
    print(myVar)
    
print(myVar)