from __future__ import division 

measurements = [ 
    ('gene1', 121, 98), 
    ('gene2', 56,  32), 
    ('gene3', 1036, 1966), 
    ('gene4', 543, 522) 
] 

def get_ratio(measurement): 
    return measurement[2] / measurement[1] 

print(sorted(measurements, key=get_ratio, reverse=True))
