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
