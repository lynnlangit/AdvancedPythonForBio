print([line[1:] for line in open('sequences.fasta') if line.startswith('>')])

print([
	line[1:] 
	for line 
	in open('sequences.fasta') 
	if line.startswith('>')])
