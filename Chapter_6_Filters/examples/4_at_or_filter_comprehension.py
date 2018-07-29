from __future__ import division

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 

ats_list = [(dna.count('A') + dna.count('T')) / len(dna) for dna in dna_list]
print'at comprehension '  + str((ats_list))

def is_at_poor(dna): 
    at = (dna.count('A') + dna.count('T')) / len(dna) 
    return at < 0.6 
 
at_poor_dna_lengths = [len(dna) for dna in dna_list if is_at_poor(dna)]
print'at filter comprehension '  + str((at_poor_dna_lengths))
