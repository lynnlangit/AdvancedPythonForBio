# ask the user for the filename, open it and read the DNA sequence
input_file = raw_input('enter filename:\n') 
f = open(input_file) 
dna = f.read().rstrip("\n") 

# ask the user for the number of pieces and calculate the piece length
pieces = int(raw_input('enter number of pieces:\n')) 
piece_length = len(dna) / pieces 
print('piece length is ' + str(piece_length)) 

# print out each piece of DNA in turn
for start in range(0, len(dna)-piece_length+1, piece_length): 
    print(dna[start:start+piece_length]) 
