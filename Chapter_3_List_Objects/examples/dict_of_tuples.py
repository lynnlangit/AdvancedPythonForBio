records = {
    'ABC123' : ('actgctagt', 1),
    'XYZ456' : ('ttaggttta', 1),
    'HIJ789' : ('cgcgatcgt', 5)
}

(my_sequence, my_code) = records.get('XYZ456')
print(my_sequence, my_code)
