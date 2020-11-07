from ncbiTAXONparser import ncbi_data_parser


ncbi_parser = ncbi_data_parser.Parser(names_file='./data/names.dmp',
                                      nodes_file='./data/nodes.dmp', interactive=False)


tax_id = 18794
taxid_set = [18794, 422320, 422327, 422329, 422331]
downtorank = 'tribe'
synonym = 'Senecio pseudoorientalis'

print('Check if taxonid {} is valid'.format(tax_id))
valid = ncbi_parser.taxid_is_valid(tax_id)
print(valid)

print('Get corresponding rank of taxonid {}'.format(tax_id))
rank = ncbi_parser.get_rank(tax_id)
print(rank)

print('get higher from taxid and rank')
df2 = ncbi_parser.get_higher_from_id(tax_id, 'tribe')
print(df2)

print('get mrca of {}'.format(taxid_set))
mrca = ncbi_parser.get_mrca(taxid_set)
print(mrca)

print('Get ID of higher rank {} for taxonid {}'.format(downtorank, tax_id))
higher_rank_id = ncbi_parser.get_downtorank_id(tax_id, downtorank=downtorank)
print(higher_rank_id)

print('Check if mrca id {} is valid'.format(mrca))
valid_mrca = ncbi_parser.check_mrca_input(mrca)
print(valid_mrca)

print('Check if taxonid {} is part of mrca'.format(tax_id, mrca))
part_of_mrca = ncbi_parser.match_id_to_mrca(tax_id, mrca)
print(part_of_mrca)

print('Get scientific name for taxonid {}'.format(tax_id))
spn = ncbi_parser.get_name_from_id(tax_id)
print(spn)

print('Get taxon id from scientific name {}'.format(spn))
id = ncbi_parser.get_id_from_name(spn)
print(id)

print('Get taxon id from synonym name {}'.format(synonym))
id_synonym = ncbi_parser.get_id_from_synonym(synonym)
print(id_synonym)

print('Get all taxon ids that are part of a higher ranked id {}'.format(tax_id))
ids = ncbi_parser.get_lower_from_id(tax_id)
print(ids)
