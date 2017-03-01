import re

def make_digester(pattern, offset): 

    def digester(dna): 
        current_position = 0 
        result = [] 
        for m in re.finditer(pattern, dna): 
            result.append(dna[current_position:m.start() + offset]) 
            current_position = m.start() + offset 
        result.append(dna[current_position:]) 
        return result 

    return digester 

dna = 'CGATGAATTCTATCGATATCGTGA'

ecori_digester = make_digester('GAATTC', 1)
print(ecori_digester(dna))

ecorv_digester = make_digester('GATATC', 3) 
print(ecorv_digester(dna)) 
