def generate_kmers(length):
    result = ['']
    for i in range(length):
        new_result = []
        for kmer in result:
            for base in ['A', 'T', 'G', 'C']:
                new_result.append(kmer + base)
        result = new_result
    for i in result:
        answer = i + " "
        print 'Some', answer

generate_kmers(1)
generate_kmers(2)
generate_kmers(3)
