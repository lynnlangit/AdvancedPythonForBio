def multiply(x,y): 
    return x * y 

def add(x,y): 
    return x + y 

numbers = [2,6,3,8,5,4] 
print'multiplier ' + str((reduce(multiply, numbers)))
print'adder ' + str((reduce(add, numbers)))
