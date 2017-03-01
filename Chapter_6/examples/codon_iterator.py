class DNASequence(): 
    position = 0 
    
    def __init__(self, sequence): 
        self.sequence = sequence 
 
 
    def __iter__(self): 
        return self 
 
    def next(self): 
        if self.position < (len(self.sequence) - 2): 
            codon = self.sequence[self.position:self.position+3] 
            self.position += 3 
            return codon 
        else: 
            raise StopIteration 
 
my_seq = DNASequence("ATGACGCTAT") 
for codon in my_seq: 
    print(codon)
