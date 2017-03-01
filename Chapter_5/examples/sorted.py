from __future__ import division 
import re 

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 

# sorted using the default order
sorted_dna = sorted(dna_list) 
print("sorted alphabetically: " + str(sorted_dna)) 
print("original list: " + str(dna_list))

# sorted by length
sorted_dna = sorted(dna_list, key=len) 
print("sorted by length: " + str(sorted_dna))

# reverse sorted by length
sorted_dna = sorted(dna_list, key=len, reverse=True)
print("reverse sorted by length: " + str(sorted_dna))

# sorted by AT content
def get_at(dna): 
    return (dna.count('A') + dna.count('T')) / len(dna) 
sorted_dna = sorted(dna_list, key=get_at) 
print("sorted by AT content: " + str(sorted_dna))

# sorted by poly-A tail length
dna_list = ['ATCGA', 'ACGG', 'CGTAAA', 'ATCGAA'] 
def poly_a_length(dna): 
    poly_a_match = re.search(r'A+$', dna) 
    if poly_a_match: 
        return len(poly_a_match.group()) 
    else: 
        return 0 
print("sorted by poly-A tail: " + str(sorted(dna_list, key=poly_a_length))) 
