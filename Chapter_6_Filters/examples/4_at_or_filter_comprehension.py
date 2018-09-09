from __future__ import division

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 

at_ratios = [(dna.count('A') + dna.count('T')) / len(dna) for dna in dna_list]
print'AT ratios '  + str((at_ratios))

def is_AT_poor(dna): 
    at = (dna.count('A') + dna.count('T')) / len(dna) 
    return at < 0.6 
 
AT_poor_dna_lengths = [len(dna) for dna in dna_list if is_AT_poor(dna)]
print'DNA lengths of poor AT ratio items '  + str((AT_poor_dna_lengths))
