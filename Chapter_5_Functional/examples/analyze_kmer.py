from __future__ import division 

def get_kmers_f(dna, k, analyze_kmer): 
    result = [] 
    for i in range(len(dna) - k +1): 
        kmer = dna[i:i+k] 
        result.append(analyze_kmer(kmer)) 
    return result 

def get_at(dna): 
    return (dna.count('A') + dna.count('T')) / len(dna) 

dna = 'ATCGATCATCGGCATCGATCGGTATCAGTACGTAC'
at_scores = get_kmers_f(dna, 8, get_at)
print(at_scores)

cg_counts = get_kmers_f(dna, 8, lambda dna : dna.count('CG'))
print(cg_counts)
