try: 
    f = open('my_file.txt') 
    try: 
        my_number = int(f.read()) 
    except ValueError: 
        print('not an integer!') 
    finally: 
        f.close() 
except IOError: 
    print('cannot open file') 
