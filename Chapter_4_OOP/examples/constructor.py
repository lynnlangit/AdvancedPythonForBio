from __future__ import division


class DNARecord(object): 
    def __init__(self, sequence, gene_name, species_name):
         self.sequence = sequence
         self.gene_name = gene_name
         self.species_name = species_name
 
    def complement(self): 
        replacement1 = self.sequence.replace('A', 't') 
        replacement2 = replacement1.replace('T', 'a') 
        replacement3 = replacement2.replace('C', 'g') 
        replacement4 = replacement3.replace('G', 'c') 
        return replacement4.upper() 
 
    def get_AT(self): 
        length = len(self.sequence) 
        a_count = self.sequence.count('A') 
        t_count = self.sequence.count('T') 
        at_content = (a_count + t_count) / length 
        return at_content 


 
d1 = DNARecord('ATATATTATTATATTATA', 'COX1', 'Homo sapiens')
print(d1.complement())
