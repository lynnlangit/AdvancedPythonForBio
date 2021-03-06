from __future__ import division

class DNARecord(object): 
    def __init__(self, sequence, gene_name, species_name):
         self.sequence = sequence
         self.gene_name = gene_name
         self.species_name = species_name
 
    def get_AT(self): 
        length = len(self.sequence) 
        a_count = self.sequence.count('A') 
        t_count = self.sequence.count('T') 
        at_content = (a_count + t_count) / length 
        return at_content 

    def get_fasta(self): 
        safe_species_name = self.species_name.replace(' ','_')
        header = '>' + self.gene_name + '_' + safe_species_name
        return header + '\n' + self.sequence + '\n' 
 
d1 = DNARecord('ATATATTATTATATTATA', 'COX1', 'Homo sapiens')
print(d1.get_fasta())
