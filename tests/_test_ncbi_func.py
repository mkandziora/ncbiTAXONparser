import os
import pandas as pd


ncbi_parser = ncbi_data_parser.Parser(names_file='./data/names.dmp',
                                      nodes_file='./data/nodes.dmp', interactive=False)

ids = ncbi_parser.get_lower_from_id(102812)
print(ids)
print(len(ids))

