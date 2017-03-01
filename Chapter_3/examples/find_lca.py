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


def find_subtrees(my_list, taxon1, taxon2): 
    result = [] 
    if contains(my_list, taxon1) and contains(my_list, taxon2): 
        result.append(my_list) 
    for sublist in my_list: 
        if isinstance(sublist, list): 
            result.extend(find_subtrees(sublist, taxon1, taxon2)) 
    return result 

def count_leaves(subtree): 
    total = 0 
    for element in subtree: 
        if isinstance(element, list): 
            total  = total + count_leaves(element) 
        else: 
            total = total + 1 
    return total 

tree = ['dog', ['raccoon','bear'], [['sea_lion','seal'],['monkey','cat'], 'weasel']]
subtrees = find_subtrees(tree, 'monkey', 'cat') 
sorted_subtrees = sorted(subtrees, key=count_leaves) 
print(sorted_subtrees[0]) 
