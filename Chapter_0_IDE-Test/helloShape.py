# This file is a simple 'Hello Python' type sample for you to use to check your IDE setup
# I am using VSCode with Python language plug-ins

def square(x):
    y = x * x
    return y

def cube(x):
    z = x * x * x
    return z

myNum = 6
toSquare = myNum
toCube = myNum

if(myNum == toSquare):
    finalSquare = square(toSquare)
    print "The result of " + str(toSquare) + " squared is " + str(finalSquare)
finalCube = cube(toCube)
print "The result of " + str(toCube) + " cubed is " + str(finalCube)    