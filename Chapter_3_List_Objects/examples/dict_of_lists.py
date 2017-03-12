dna = 'aattggaattggaattg'
k = 4 
kmer2list = {} 
for start in range(len(dna) - k + 1): 
    kmer = dna[start:start + k] 
    list_of_positions = kmer2list.get(kmer, []) 
    list_of_positions.append(start) 
    kmer2list[kmer] = list_of_positions 
print(kmer2list)
