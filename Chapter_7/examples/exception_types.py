try: 
    f = open('my_file.txt') 
    my_number = int(f.read()) 
    print(my_number + 5) 
except IOError: 
    print("sorry, couldn't find the file") 
except ValueError: 
    print("sorry, couldn't parse the number") 
