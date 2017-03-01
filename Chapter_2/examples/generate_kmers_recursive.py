def generate_kmers_rec(length): 
    if length == 1: 
        return ['A', 'T', 'G', 'C'] 
    else: 
        result = [] 
        for seq in generate_kmers_rec(length - 1): 
            for base in ['A', 'T', 'G', 'C']: 
                result.append(seq + base) 
        return result 
