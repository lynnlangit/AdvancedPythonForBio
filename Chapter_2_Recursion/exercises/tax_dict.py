# Preparing to refactor - remove all lists from Ch2 and reference 
# from one external class file
# test and update all print statements to be return statements

class requiredLists(object):

    global tax_dict_1 
    tax_dict_1 = { 
    'aaa' : 'bbb',       'ccc' : 'ddd',
    'Pan troglodytes' : 'Hominoidea',       'Pongo abelii' : 'Hominoidea', 
    'Hominoidea' :  'Simiiformes',          'Simiiformes' : 'Haplorrhini', 
    'Tarsius tarsier' : 'Tarsiiformes',     'Haplorrhini' : 'Primates',
    'Tarsiiformes' : 'Haplorrhini',         'Loris tardigradus' : 'Lorisidae',
    'Lorisidae' : 'Strepsirrhini',          'Strepsirrhini' : 'Primates',
    'Allocebus trichotis' : 'Lemuriformes', 'Lemuriformes' : 'Strepsirrhini',
    'Galago alleni' : 'Lorisiformes',       'Lorisiformes' : 'Strepsirrhini',
    'Galago moholi' : 'Lorisiformes'
    } 

    def makeList(tax_dict_1):
        myList = tax_dict_1
        return 'List' + str(myList)
    
    def printList(tax_dict_1):      # returns unsorted
        myList = tax_dict_1
        print 'List' + str(myList)

    makeList(tax_dict_1)
    printList(tax_dict_1)

