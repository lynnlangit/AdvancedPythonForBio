from __future__ import division

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 

ats_list = [(dna.count('A') + dna.count('T')) / len(dna) for dna in dna_list]
print'AT comprehension '  + str((ats_list))

def is_AT_poor(dna): 
    at = (dna.count('A') + dna.count('T')) / len(dna) 
    return at < 0.6 
 
AT_poor_dna_lengths = [len(dna) for dna in dna_list if is_AT_poor(dna)]
print'AT filter comprehension '  + str((AT_poor_dna_lengths))
