from __future__ import division

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 

ats = [(dna.count('A') + dna.count('T')) / len(dna) for dna in dna_list]

print(ats)
