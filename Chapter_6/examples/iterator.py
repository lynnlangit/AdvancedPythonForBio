class DNASequence(): 
    def __init__(self, sequence): 
        self.sequence = sequence 
 
 
    def __iter__(self): 
        return iter(self.sequence) 
 
my_seq = DNASequence("ATGACGCTAT") 
for base in my_seq: 
    print(base)
