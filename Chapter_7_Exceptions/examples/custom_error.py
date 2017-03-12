import re

class AmbiguousBaseError(Exception): 
    pass 

def get_at_content(dna): 
    if re.search(r'[^ATGC]', dna): 
        raise AmbiguousBaseError('Sequence cannot contain non-ATGC bases') 
    length = len(dna) 
    a_count = dna.count('A') 
    t_count = dna.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content 
 
sequences = ['ACGTACGTGAC', 'ACTGCTNAACT', 'ATGGCGCTAGC'] 
for seq in sequences: 
    try: 
        print('AT content for ' + seq + ' is ' + str(get_at_content(seq)))
    except AmbiguousBaseError: 
        print('skipping invalid sequence '+ seq) 
