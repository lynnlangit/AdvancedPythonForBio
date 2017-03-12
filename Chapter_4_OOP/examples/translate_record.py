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


def translate_dna(dna_record): 
    gencode = { 
	    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
	    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
	    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 
	    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
	    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
	    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
	    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
	    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
	    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
	    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'} 
    last_codon_start = len(dna_record.sequence) - 2 
    protein = "" 
    for start in range(0,last_codon_start,3): 
        codon = dna_record.sequence[start:start+3] 
        aa = gencode.get(codon.upper(), 'X') 
        protein = protein + aa 
    return protein
 
d1 = DNARecord('ATATATTATTATATTATA', 'COX1', 'Homo sapiens')
print(translate_dna(d1))
