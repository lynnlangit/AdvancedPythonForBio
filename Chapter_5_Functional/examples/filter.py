from __future__ import division 

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 

long_dna = []           # 1. using procedural code
for dna in dna_list: 
    if len(dna) > 5: 
        long_dna.append(dna) 
print 'using procedural code for long DNA ' + ', '.join(long_dna)

def get_at(dna): 
    return (dna.count('A') + dna.count('T')) / len(dna) 

at_poor_dna = [] 
for dna in dna_list: 
    if (dna.count('A') + dna.count('T')) / len(dna) < 0.6: 
        at_poor_dna.append(dna) 
print 'using procedural code for poor DNA ' + ', '.join(at_poor_dna)

def is_long(dna):       # 2. using filter
    return len(dna) > 5 
 
long_dna = filter(is_long, dna_list) 
print 'using filter for long DNA ' + ', '.join(long_dna)

def is_at_poor(dna): 
    at = (dna.count('A') + dna.count('T')) / len(dna) 
    return at < 0.6 
 
at_poor_dna = filter(is_at_poor, dna_list) 
print 'using filter for poor DNA ' + ', '.join(at_poor_dna)
