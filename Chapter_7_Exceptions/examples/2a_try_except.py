try: 
    #f = open('blast_result.txt') 
    f = open('misssing.txt') 
    print('file contents: ' + f.read())
except: 
    print("sorry, couldn't find the file") 
