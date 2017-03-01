from __future__ import division

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 

# using procedural code

lengths = [] 
for dna in dna_list: 
    lengths.append(len(dna)) 
print(lengths)

at_contents = [] 
for dna in dna_list: 
    at_contents.append((dna.count('A') + dna.count('T')) / len(dna)) 
print(at_contents)

# using map

def get_at(dna): 
    return (dna.count('A') + dna.count('T')) / len(dna) 

lengths = map(len, dna_list) 
print(lengths)
at_contents = map(get_at, dna_list) 
print(at_contents)
at_contents = map( 
    lambda dna : (dna.count('A') + dna.count('T')) / len(dna), 
    dna_list 
)
print(at_contents)
