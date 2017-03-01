from __future__ import division

class ProteinRecord(object): 
 
    def __init__(self, sequence, gene_name, species_name): 
        self.sequence = sequence 
        self.gene_name = gene_name 
        self.species_name = species_name 
 
    def get_fasta(self): 
        safe_species_name = self.species_name.replace(' ','_') 
        header = '>' + self.gene_name + '_' + safe_species_name 
        return header + '\n' + self.sequence + '\n' 
 
    def get_hydrophobic(self): 
        aa_list=['A','I','L','M','F','W','Y','V'] 
        protein_length = len(self.sequence) 
        total = 0 
        for aa in aa_list: 
            aa = aa.upper() 
            aa_count = self.sequence.count(aa) 
            total = total + aa_count 
        percentage = total * 100 / protein_length 
        return percentage


d1 = ProteinRecord('MSRSLLLRFLLFLLLLPPLP', 'COX1', 'Homo sapiens') 
print(d1.get_fasta()) 
print(str(d1.get_hydrophobic()))
