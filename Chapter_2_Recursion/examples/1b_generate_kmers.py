def generate_kmers(length):
    result = ['']
    for i in range(length):
        new_result = []
        for kmer in result:
            next_result = []
            for four in result:
                for base in ['A', 'T', 'G', 'C']:
                    next_result.append(four + base)
        result =  new_result + next_result
    for i in result:
        answer = i + " "
        print 'Some kmer', answer

generate_kmers(1)
generate_kmers(2)
generate_kmers(3)
generate_kmers(4)