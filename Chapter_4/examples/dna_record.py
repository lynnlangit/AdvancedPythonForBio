from __future__ import division

class DNARecord(object): 
    sequence = 'ACGTAGCTGACGATC'
    gene_name = 'ABC1'
    species_name = 'Drosophila melanogaster'
 
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

d = DNARecord()
print('Created a record for ' + d.gene_name + ' from ' + d.species_name)
print('AT is ' + str(d.get_AT()))
print('complement is ' + d.complement())
