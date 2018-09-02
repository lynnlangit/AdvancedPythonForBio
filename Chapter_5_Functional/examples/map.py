from __future__ import division

dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 
lengths = [] 

# using procedural code
for dna in dna_list: 
    lengths.append(len(dna)) 
print("Segment lengths via 'for loop': " +str(lengths))

at_contents = [] 
for dna in dna_list: 
    at_contents.append((dna.count('A') + dna.count('T')) / len(dna)) 
print("AT-rate via 'for loop ': " + str(at_contents) + '\n')

# using map
def get_at(dna): 
    return (dna.count('A') + dna.count('T')) / len(dna) 

lengths = map(len, dna_list) 
print("Segment lengths via 'map function': " +str(lengths))

at_contents = map(get_at, dna_list) 
print("AT-rate via 'map function': " + str(at_contents))

at_contents = map(lambda dna : (dna.count('A') + dna.count('T')) / len(dna), dna_list )
print("AT-rate via 'map lambda': "+ str(at_contents))
