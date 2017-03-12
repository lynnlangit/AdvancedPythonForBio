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


def get_ancestors(taxon):
	print('calculating ancestors for ' + taxon)
	if taxon == 'Primates':
		print('taxon is Primates, returning an empty list')
		return []
	else:
		print('taxon is not Primates, looking up the parent')
		parent = tax_dict.get(taxon)
		print('the parent is ' + parent + ' ')
		print('looking up ancestors for ' + parent)
		parent_ancestors = get_ancestors(parent)
		print('parent ancestors are ' + str(parent_ancestors))
		result = [parent] + parent_ancestors 
		print('about to return the result: ' + str(result)) 
		return result

get_ancestors('Galago alleni')
