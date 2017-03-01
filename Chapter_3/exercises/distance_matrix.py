from __future__ import division
from collections import defaultdict

gene_sets = { 
        'arsenic' : {1,2,3,4,5,6,8,12}, 
        'cadmium' : {2,12,6,4}, 
        'copper' : {7,6,10,4,8}, 
        'mercury' : {3,2,4,5,1} 
} 

similarity_scores = defaultdict(dict)
for condition1, set1 in gene_sets.items(): 
   for condition2, set2 in gene_sets.items(): 
      if condition1 != condition2: 
         similarity = len(set1.intersection(set2)) / len(set1.union(set2))
         similarity_scores[condition1][condition2] = similarity 


