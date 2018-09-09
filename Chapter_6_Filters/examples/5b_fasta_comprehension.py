one= ("this is one: " + str([
	line[0:] 
	for line 
	in open('sequences.fasta') 
	if line.startswith('>')]))

two = ("this is two: " + str([
	line[1:] 
	for line 
	in open('sequences.fasta') 
	if line.startswith('>')]))

print(one.capitalize()) +'\n'
print(two.capitalize()) +'\n'


