from __future__ import division

def get_AT(my_dna): 
    length = len(my_dna) 
    a_count = my_dna.count('A') 
    t_count = my_dna.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content 
 
def complement(my_dna): 
    replacement1 = my_dna.replace('A', 't') 
    replacement2 = replacement1.replace('T', 'a') 
    replacement3 = replacement2.replace('C', 'g') 
    replacement4 = replacement3.replace('G', 'c') 
    return replacement4.upper() 

dna_sequence = "ACTGATCGTTACGTACGAGTCAT" 
species = "Drosophila melanogaster"
gene_name = "ABC1"
print("Looking at the " + species + " " + gene_name + " gene")
print("AT content is " + str(get_AT(dna_sequence))) 
print("complement is " + complement(dna_sequence)) 
