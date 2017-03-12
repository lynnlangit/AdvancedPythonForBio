from __future__ import division
import re

class SequenceRecord(object): 
 
    def __init__(self, sequence, gene_name, species_name): 
 	if not re.match(r'[A-Z][a-z]+ [a-z]+', species_name): 
	    exit(species_name + ' is not a valid species name!')		 
        self.sequence = sequence 
        self.gene_name = gene_name 
        self.species_name = species_name 
 
    def get_fasta(self): 
        safe_species_name = self.species_name.replace(' ','_') 
        header = '>' + self.gene_name + '_' + safe_species_name 
        return header + '\n' + self.sequence + '\n' 
 
class ProteinRecord(SequenceRecord): 
    
	def get_hydrophobic(self): 
		aa_list=['A','I','L','M','F','W','Y','V'] 
		protein_length = len(self.sequence) 
		total = 0 
		for aa in aa_list: 
		    aa = aa.upper() 
		    aa_count = self.sequence.count(aa) 
		    total = total + aa_count 
		return total * 100 / protein_length  
 
class DNARecord(SequenceRecord): 

    def __init__(self, sequence, gene_name, species_name, genetic_code): 

        # first call the SequenceRecord constructor to check the species name
        # and set the sequence, gene_name and species_name variables
        SequenceRecord.__init__(self, sequence, gene_name, species_name) 

        # now set the genetic code variable
        self.genetic_code = genetic_code 
 
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
        return (a_count + t_count) / length 

d1 = DNARecord('ATCGCGTACGTGATCGTAG', 'COX1', 'Homo sapiens', 5) 
print(d1.get_fasta()) 
print(d1.complement()) 
print('genetic code is ' + str(d1.genetic_code))
