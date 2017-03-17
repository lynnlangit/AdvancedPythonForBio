import re

class InvalidCharacterError(Exception):
    pass
class InvalidBaseError(InvalidCharacterError):
    pass
class InvalidAminoAcidError(InvalidCharacterError):
    pass

class SequenceRecord(object):

    def __init__(self, sequence, gene_name, species_name):

        if not isinstance(gene_name, str):
            raise TypeError('gene name must be a string')

        if len(gene_name) == 0:
            raise ValueError('gene name cannot be empty')

        if not re.match(r"[A-Z][a-z]+ [a-z]+", species_name):
            raise ValueError('species name incorrectly formatted')

        self.validate_sequence(sequence)
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name

    def get_fasta(self):
        return('getting fasta sequence')

class ProteinRecord(SequenceRecord):

    # sequence validation method to check for invalid AA residue codes
    def validate_sequence(self, sequence):
        if re.search(r'[^FLSYCWPHQRIMTNKVADEG]', sequence):
            raise InvalidAminoAcidError("invalid amino acid code in sequence")

    def get_hydrophobic(self):
        return('getting hydrophobic')

class DNARecord(SequenceRecord):

    def validate_sequence(self, sequence):
        if re.search(r'[^ATGC]', sequence):
            raise InvalidBaseError("invalid base in sequence")

    def complement(self):
        return('getting complement')

    def get_AT(self):
        return('getting AT')

