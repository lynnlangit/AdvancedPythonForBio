from __future__ import division 

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 
def get_at_ratio(dna): 
     return (dna.count('A') + dna.count('T')) / len(dna)

d = { x : get_at_ratio(x) for x in dna_list }
print 'DNA value: AT ratio ' + str(d)
