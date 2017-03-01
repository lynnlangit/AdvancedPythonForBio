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

def get_children_rec(taxon): 
    result = [taxon] 
    children = new_tax_dict.get(taxon, []) 
    for child in children: 
        result.extend(get_children_rec(child)) 
    return result 

print(get_children_rec('Strepsirrhini'))

