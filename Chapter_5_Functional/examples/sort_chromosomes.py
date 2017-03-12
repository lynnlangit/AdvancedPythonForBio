loci = [ 
    (4, 9200, 'gene1'), 
    (6, 63788, 'gene2'), 
    (4, 7633, 'gene3'), 
    (2, 8766, 'gene4') 
]

def get_chromosome(locus): 
    return locus[0] 
 
def get_base_position(locus): 
    return locus[1] 

sorted_by_base = sorted(loci, key=get_base_position) 
final_sort = sorted(sorted_by_base, key=get_chromosome) 
print(final_sort)  
