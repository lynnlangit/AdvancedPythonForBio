import os 
import sys 
 
# check for valid filename
input_file = raw_input('enter filename:\n') 
if not os.path.isfile(input_file): 
    sys.exit('not a valid filename') 
f = open(input_file) 
dna = f.read().rstrip("\n") 

# check for valid number
pieces = raw_input('enter number of pieces:\n') 
if not pieces.isdigit(): 
    sys.exit('not a valid number') 

# check that number is not zero or negative
pieces = int(pieces) 
if pieces < 0: 
    sys.exit('number of pieces must be greater than zero') 

# do the processing
piece_length = len(dna) / pieces 
print('piece length is ' + str(piece_length)) 
for start in range(0, len(dna)-piece_length+1, piece_length): 
    print(dna[start:start+piece_length]) 
