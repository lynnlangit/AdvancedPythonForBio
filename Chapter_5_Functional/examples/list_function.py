def print_list_with_function(my_list, my_function): 
    for element in my_list: 
        print(my_function(element)) 

# using a built-in function
input = ['abc', 'defhij', 'kl'] 
print_list_with_function(input, len) 

# using a custom function
def get_second(input): 
    return input[1] 
print_list_with_function(input, get_second)

# using a lambda expression
print_list_with_function(input, lambda(input) : input[1] )
