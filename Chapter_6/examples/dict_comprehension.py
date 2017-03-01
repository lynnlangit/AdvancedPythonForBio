from __future__ import division 

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 
def get_at(dna): 
     return (dna.count('A') + dna.count('T')) / len(dna) 

d = { x : get_at(x) for x in dna_list }
print(d)
