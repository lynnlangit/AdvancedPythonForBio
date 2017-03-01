try: 
    f = open('my_file.txt') 
    my_number = int(f.read()) 
except IOError as ex: 
    print("sorry, couldn't find the file: " + ex.strerror) 
except ValueError as ex: 
    print("sorry, couldn't parse the number: " +  ex.args[0]) 
else:
    print(my_number + 5) 
