from __future__ import division

gene_sets = { 
        'arsenic' : {1,2,3,4,5,6,8,12}, 
        'cadmium' : {2,12,6,4}, 
        'copper' : {7,6,10,4,8}, 
        'mercury' : {3,2,4,5,1} 
} 

similarity_scores = {
    c1: {
        c2 : len(s1.intersection(s2)) / len(s1.union(s2)) 
        for c2,s2 in gene_sets.items() 
        if c1 != c2
        } 
    for c1,s1 in gene_sets.items()
} 

print(similarity_scores)
