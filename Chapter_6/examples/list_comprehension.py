dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG']

# generate a list of lengths using procedural code
lengths = []
for dna in dna_list:
    lengths.append(len(dna))
print(lengths)

# do the same with a map()
lengths = map(len, dna_list) 
print(lengths)

# do the same with a list comprehension
lengths = [len(dna) for dna in dna_list] 
print(lengths)
