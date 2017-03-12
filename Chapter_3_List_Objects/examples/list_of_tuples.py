records = [
    ('actgctagt', 'ABC123', 1),
    ('ttaggttta', 'XYZ456', 1),
    ('cgcgatcgt', 'HIJ789', 5)
]

for record in records:
    (this_sequence, this_accession, this_code) = record
    print('accession number : ' + this_accession)
    print('genetic code: ' + str(this_code)) 
