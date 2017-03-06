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