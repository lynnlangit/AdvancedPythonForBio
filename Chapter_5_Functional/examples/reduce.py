numbers = [2,6,3,8,5,4] 

def multiply(x,y): 
    return x * y 

def add(x,y): 
    return x + y 

def subtract(x,y): 
    return x - y 

def divide(x,y): 
    return x / y 

print'multiplier ' + str((reduce(multiply, numbers)))
print'adder ' + str((reduce(add, numbers)))
print'subtractor ' + str((reduce(subtract, numbers)))
print'divider ' + str((reduce(divide, numbers)))
