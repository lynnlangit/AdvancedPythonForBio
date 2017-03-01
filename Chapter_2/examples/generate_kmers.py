def generate_kmers(length): 
    result = [''] 
    for i in range(length): 
        new_result = [] 
        for kmer in result: 
            for base in ['A', 'T', 'G', 'C']: 
                new_result.append(kmer + base) 
        result = new_result 
    return result 
