def get_4mers(dna):
	result = [] 
	for i in range(len(dna) - 3): 
    		result.append(dna[i:i+4]) 
	return result

def generate_4mers(dna): 
    for i in range(len(dna) - 3): 
        yield dna[i:i+4] 

for x in get_4mers('actggcgtgcatg'): 
    print(x)
for x in generate_4mers('actggcgtgcatg'): 
    print(x)
