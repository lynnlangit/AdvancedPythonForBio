try: 
    f = open('my_file.txt') 
    my_number = int(f.read()) 
    print(my_number + 5) 
except IOError as ex: 
    print("sorry, couldn't find the file: " + ex.strerror) 
except ValueError as ex: 
    print("sorry, couldn't parse the number: " +  ex.args[0]) 
