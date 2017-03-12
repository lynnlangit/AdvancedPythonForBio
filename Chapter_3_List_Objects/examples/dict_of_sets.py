gene_sets = {
    'arsenic' : {1,2,3,4,5,6,8,12},
    'cadmium' : {2,12,6,4},
    'copper' : {7,6,10,4,8},
    'mercury' : {3,2,4,5,1}
}

for condition1,set1 in gene_sets.items(): 
     for condition2,set2 in gene_sets.items(): 
         if set1.issubset(set2) and condition1 != condition2: 
             print(condition1 + ' is a subset of ' + condition2)   
