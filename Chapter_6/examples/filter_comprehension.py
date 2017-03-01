dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG']
lengths = [len(dna) for dna in dna_list if dna.startswith('A')] 
print(lengths)
