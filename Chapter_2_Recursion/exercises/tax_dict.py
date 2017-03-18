# Preparing to refactor - remove all lists from Ch2 and reference 
# from one external class file
# test and update all print statements to be return statements

class requiredLists(object):

    tax_dict = { 
    'Pan troglodytes' : 'Hominoidea',       'Pongo abelii' : 'Hominoidea', 
    'Hominoidea' :  'Simiiformes',          'Simiiformes' : 'Haplorrhini', 
    'Tarsius tarsier' : 'Tarsiiformes',     'Haplorrhini' : 'Primates',
    'Tarsiiformes' : 'Haplorrhini',         'Loris tardigradus' : 'Lorisidae',
    'Lorisidae' : 'Strepsirrhini',          'Strepsirrhini' : 'Primates',
    'Allocebus trichotis' : 'Lemuriformes', 'Lemuriformes' : 'Strepsirrhini',
    'Galago alleni' : 'Lorisiformes',       'Lorisiformes' : 'Strepsirrhini',
    'Galago moholi' : 'Lorisiformes'
    } 

    def makeList(tax_dict):
        myList = tax_dict
        print 'List' + str(myList)

    def makeMe(me):
        the = me
        return "I am " + the

    makeMe("Lynn")
    makeList(tax_dict)