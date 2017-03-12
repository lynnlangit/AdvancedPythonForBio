# Run in terminal
# ask the user for the filename, open it and read the DNA sequence - alleles.csv
input_file = raw_input('enter filename:\n') 
f = open(input_file) 
dna = f.read().rstrip("\n") 

# ask the user for the number of pieces and calculate the piece length - 853
pieces = int(raw_input('enter number of pieces:\n')) 
piece_length = len(dna) / pieces 
print('piece length is ' + str(piece_length)) 

for start in range(0, len(dna)-piece_length+1, piece_length): 
    print(dna[start:start+piece_length]) 
