from __future__ import division


# function to return the percent identity of a hit
def get_percent_id(hit_string):
    return float(hit_string.split("\t")[2])

# function to test whether the subject name of a hit contains COX1
def cox1_filter(hit_string):
    subject = hit_string.split("\t")[1]
    if "COX1" in subject:
        return True
    else:
        return False

# function to calculate the query start : length ratio of a hit
def start_ratio(hit_string):
    query_start = int(hit_string.split("\t")[6])
    hit_length = int(hit_string.split("\t")[3])
    return query_start / hit_length

# filter out the comment lines from the input file to leave only the hit lines
# hit_lines = filter(comment_filter, open('blast_result.txt'))
hit_lines = [line for line in open('blast_result.txt') if not line.startswith('#')]

# how many hits have fewer than 20 mismatches?
few_mismatch_hits = [
	line 
	for line 
	in hit_lines 
	if int(line.split("\t")[4]) < 20]
print("number of hits with < 20 mismatchs: " + str(len(few_mismatch_hits)))

# for matches where the subject sequence name contains COX1, list the query
# start divided by the length
cox1_hits = filter(cox1_filter, hit_lines)
print("query start / length for COX1 hits:")
for ratio in map(start_ratio, cox1_hits):
    print(ratio)

ratios = [
    int(l.split("\t")[6]) / int(l.split("\t")[3])
    for l in hit_lines
    if "COX1" in l.split("\t")[1]
]
print(ratios)
