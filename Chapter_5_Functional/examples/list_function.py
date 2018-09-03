def print_list_with_my_function(my_list, my_function): 
    for element in my_list: 
        print(my_function(element))

input = ['abc', 'defhij', 'kl'] 

print ('element group count with built-in len function')
print_list_with_my_function(input, len) 

def get_second_element(input): 
    return input[1] 
print ('2nd element using custom function')
print_list_with_my_function(input, get_second_element)

print ('ALT: 2nd element using lambda expression')
print_list_with_my_function(input, lambda(input) : input[1] )
