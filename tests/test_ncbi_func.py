import os
import pandas as pd
from ncbiTAXONparser import ncbi_data_parser


def test_functionality():

    ncbi_parser = ncbi_data_parser.Parser(names_file='./data/names.dmp',
                                          nodes_file='./data/nodes.dmp', interactive=False)

    # ids = ncbi_parser.get_lower_from_id(102812)
    # assert len(ids) == 1656

    valid = ncbi_parser.taxid_is_valid(102812)
    print(valid)
    assert valid is True


def test_get_mrca():
    tax_set = {98691, 4233, 4238, 122010, 189211, 379293, 1532448, 41633, 98722, 13480, 41640, 259884, 13361, 41654, 415159, 189254, 313929, 130253, 220498, 219103, 496614, 84585, 418283, 320626, 118770, 76276, 904565, 434677, 375931}
    ncbi_parser = ncbi_data_parser.Parser(names_file='./data/names.dmp',
                                          nodes_file='./data/nodes.dmp', interactive=False)

    mrca = ncbi_parser.get_mrca(tax_set)
    assert mrca == 4210
