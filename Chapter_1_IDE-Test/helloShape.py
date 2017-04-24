# This file is a simple 'Hello Python' type sample for you to use to check your IDE setup
# I am using VSCode with Python language plug-ins

def adder(x):
    w = x + x
    return w

def square(x):
    y = x * x
    return y

def cube(x):
    z = x * x * x
    return z

myNum = 5
toAdder = myNum
toSquare = myNum + 2
toCube = myNum

if(toAdder == 5):
    finalAdder = adder(toAdder)
    print "The result of " + str(toAdder) + " added is " + str(finalAdder)
    if(toSquare == 7):
        finalSquare = square(toSquare)
        print "The result of " + str(toSquare) + " squared is " + str(finalSquare)
finalCube = cube(toCube)
print "The result of " + str(toCube) + " cubed is " + str(finalCube)    