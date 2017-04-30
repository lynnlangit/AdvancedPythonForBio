from __future__ import division

def mismatch_filter(hit_string):
    mismatch_count = int(hit_string.split("\t")[4])
    return mismatch_count < 20

def comment_filter(line):
    return not line.startswith('#')

def get_percent_id(hit_string):
    return float(hit_string.split("\t")[2])

def get_subject(hit_string):
    return hit_string.split("\t")[1]

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

hit_lines = filter(comment_filter, open('blast_result.txt'))

few_mismatch_hits = filter(mismatch_filter, hit_lines)
print("number of hits with < 20 mismatchs: " + str(len(few_mismatch_hits)))

hits_sorted_by_percent_id = sorted(hit_lines, key=get_percent_id)
low_id_hits = hits_sorted_by_percent_id[0:10]
print("subject sequence names for low id hits:")
for subject in map(get_subject, low_id_hits):
    print(subject)

cox1_hits = filter(cox1_filter, hit_lines)
print("query start / length for COX1 hits:")
for ratio in map(start_ratio, cox1_hits):
    print(ratio)

