try: 
    #f = open('my_file.txt')      # no file
    f = open('blast_result.txt')  # invalid
    try: 
        my_number = int(f.read()) 
    except ValueError: 
        print('not an integer!') 
    finally: 
        f.close() 
except IOError: 
    print('cannot open file') 
