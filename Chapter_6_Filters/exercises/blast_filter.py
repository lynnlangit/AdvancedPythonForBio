from __future__ import division

def get_percent_id(hit_string):
    return float(hit_string.split("\t")[2])

def cox1_filter(hit_string):
    subject = hit_string.split("\t")[1]
    if "COX1" in subject:
        return True
    else:
        return False

def start_ratio(hit_string):
    query_start = int(hit_string.split("\t")[6])
    hit_length = int(hit_string.split("\t")[3])
    return query_start / hit_length

hit_lines = [line for line in open('blast_result.txt') if not line.startswith('#')]

few_mismatch_hits = [
	line 
	for line 
	in hit_lines 
	if int(line.split("\t")[4]) < 20]
print("number of hits with < 20 mismatchs: " + str(len(few_mismatch_hits))) + '\n'

cox1_hits = filter(cox1_filter, hit_lines)
for ratio in map(start_ratio, cox1_hits):
    print"query start / length for COX1 hits: "+ str((ratio)) 

ratios = [
    int(l.split("\t")[6]) / int(l.split("\t")[3])
    for l in hit_lines
    if "COX1" in l.split("\t")[1]
]
print'Ratios ' + str((ratios))
