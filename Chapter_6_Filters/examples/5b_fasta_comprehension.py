print("this is one: " + str([
	line[1:] 
	for line 
	in open('sequences.fasta') 
	if line.startswith('>')]))

print("this is two: " + str([
	line[0:] 
	for line 
	in open('sequences.fasta') 
	if line.startswith('>')]))
