dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG']

lengths = []
for dna in dna_list:
    lengths.append(len(dna))
print'Lengths using procedural code ' + str((lengths))

lengths = map(len, dna_list) 
print'Lengths using a map function ' + str((lengths))

lengths = [len(dna) for dna in dna_list] 
print'Lengths using a list comprehension ' + str((lengths))

lengths = [len(dna) for dna in dna_list if dna.startswith('A')] 
print'Lengths using a filter comprehension ' + str((lengths))
