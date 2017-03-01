new_tax_dict = { 
    'Primates': ['Haplorrhini', 'Strepsirrhini'], 
    'Tarsiiformes': ['Tarsius tarsier'], 
    'Haplorrhini': ['Tarsiiformes', 'Simiiformes'], 
    'Simiiformes': ['Hominoidea'], 
    'Lorisidae': ['Loris tardigradus'], 
    'Lemuriformes': ['Allocebus trichotis'], 
    'Lorisiformes': ['Galago alleni','Galago moholi'], 
    'Hominoidea': ['Pongo abelii', 'Pan troglodytes'], 
    'Strepsirrhini': ['Lorisidae', 'Lemuriformes', 'Lorisiformes'] 
} 

def get_children(taxon): 
    result = [] 
    stack = [taxon] 
    while len(stack) != 0: 
        current_taxon = stack.pop() 
        current_taxon_children = new_tax_dict.get(current_taxon, []) 
        stack.extend(current_taxon_children) 
        result.append(current_taxon) 
 
    return result 

print(get_children('Strepsirrhini'))

