records = [
    {'name' : 'actgctagt', 'accession' : 'ABC123', 'genetic_code' : 1},
    {'name' : 'ttaggttta', 'accession' : 'XYZ456', 'genetic_code' : 1},
    {'name' : 'cgcgatcgt', 'accession' : 'HIJ789', 'genetic_code' : 5}
]

for record in records:
    print('accession number : ' + record['accession'])
    print('genetic code: ' + str(record['genetic_code'])) 
