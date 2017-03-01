from __future__ import division
import random
import timeit
import multiprocessing

# randomly generate a list of 100 DNA sequences of length 10000 bases
dna = lambda x : ''.join([random.choice(['A', 'T', 'G', 'C']) for i in range(x)])
dna_list = [dna(10000) for x in range(1000)]

def get_kmers(dna, k):
	kmers = [] 
	for i in range(len(dna) - k +1): 
    		kmers.append(dna[i:i+k]) 
	return kmers

def get_at_content(dna): 
    length = len(dna) 
    a_count = dna.count('A') 
    t_count = dna.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content 

def get_variance(dna):
	ats = map(get_at_content, get_kmers(dna, 10))
	mean  = sum(ats) / len(ats)
	square_diffs = map(lambda at :(at - mean) ** 2, ats)
	mean_square_diff = sum(square_diffs) / len(square_diffs)
	return mean_square_diff

# create a pool of processes - experiement with different numbers
pool = multiprocessing.Pool(8)

# time how long it takes to calculate the variances 
start_time = timeit.default_timer()
variances = pool.map(get_variance, dna_list)
elapsed = timeit.default_timer() - start_time
print(elapsed)
