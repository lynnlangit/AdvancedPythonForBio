def contains(my_list, target): 
    result = False 
    for element in my_list: 
        if isinstance(element, list): 
            if contains(element, target): 
                result = True 
        else: 
            if element == target: 
                result = True 
    return result 


assert contains([1,2,3], 2)
assert contains([1,[2,3],[4,5]], 5)
assert contains([['sea_lion','seal'],['monkey','cat'], 'weasel'], 'cat')
