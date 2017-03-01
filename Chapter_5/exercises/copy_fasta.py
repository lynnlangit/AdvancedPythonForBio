from __future__ import division
import re
def do_nothing(x):
    return x
def fasta_copy(
 source,
 destination,
 process_header=lambda x: x,
 process_sequence=lambda x: x
 ):
    output = open(destination, "w")
    header = ""
    for line in open(source):
        if line.startswith('>'):
            header = line.rstrip("\n")[1:]
        else:
            sequence = process_sequence(line.rstrip("\n"))
            new_header = process_header(header, sequence)
            output.write('>' + new_header +"\n")
            output.write(sequence + "\n")


def to_upper(dna):
    return dna.upper()

def remove_unknown(dna):
    return re.sub(r'[^ATGCatgc]', '',dna)

def fix_spaces(header, sequence):
    return header.replace(' ', '_')

def truncate(header, sequence):
    return header[0:10]

def append_length(header, sequence):
    return header + '_' + str(len(sequence))

def get_at(dna):
        return (dna.count('A') + dna.count('T')) / len(dna)

def append_at(header, sequence):
    return header + '_' + str(get_at(sequence))

def check_transcript(header, sequence):
    if re.search(r'^ATG.*A{5,}$', sequence):
        return header + ' (putative transcript)'
    else:
        return header

# change the process_header and/or process_sequence varaibles in this function call
fasta_copy('sequences.fasta', 'corrected.fasta', process_header=check_transcript)
