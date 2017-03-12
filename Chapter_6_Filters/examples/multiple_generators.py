class DNASequence(): 
 
    def __init__(self, sequence): 
        self.sequence = sequence 
 
    def bases(self): 
        return iter(self.sequence) 
 
    def codons(self): 
        for i in range(0, len(self.sequence) -2, 3): 
             yield self.sequence[i:i+3] 
 
    def kmers(self, k): 
        for i in range(len(self.sequence) - k +1): 
            yield self.sequence[i:i+k] 
      
my_seq = DNASequence("atgccgcat") 
for base in my_seq.bases(): 
    print(base) 
for codon in my_seq.codons(): 
    print(codon) 
for kmer in my_seq.kmers(5): 
    print(kmer)
