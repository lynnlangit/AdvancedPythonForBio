def generate_primers(length):
    if length == 1:
        for base in ['A', 'T', 'G', 'C']:
            yield(base)
    else:
        for seq in generate_primers(length - 1):
            for base in ['A', 'T', 'G', 'C']:
                yield(seq+base)

def generate_pairs(length):
    for forward in generate_primers(length):
        for reverse in generate_primers(length):
            yield(forward, reverse)


for f, r in generate_pairs(4):
    print(f,r)
