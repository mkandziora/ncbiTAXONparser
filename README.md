[![Build Status](https://travis-ci.com/mkandziora/ncbiTAXONparser.svg?token=tcUKPEqrpyvHbPasst5i&branch=master)](https://travis-ci.com/mkandziora/ncbiTAXONparser)

    
# ncbiTAXONparser

ncbiTAXONparser is a command-line tool written in python3 to translate names, ids and hierachical ranks for the ncbi taxonomy. The package provides tools to wrangle with the taxonomy which is a common tasks in comparative genomics and phylogenetics.
For example, it can retrieve the most recent common ancestor according to ncbi for a list of identifiers or get all taxonomic identifiers that are part of a particular tribe.

It provides the same operations as most tools available currently but connects them in a different way to improve usability. 
New functionality includes: get all lower taxon ID's for a provided taxon ID, get the most recent common ancestor of a set of taxon ID's, and check if a given taxon ID is part of a provided mrca. There are nine main functions provided to get taxonomic information, some internal functions are altered from ncbitax2lin to provide new functionality.

* `taxid\_is\_valid`: Checks if input taxon ID is known by ncbi.
* `get\_name\_from\_id`: Find the scientific name for a given ID.
* `get\_id\_from\_name`: Get the taxon ID for a given name.
* `get\_id\_from\_synonym`: Checks if provided name is a synonym and returns the valid taxon ID. Also used internally by \texttt{get\_id\_from\_name}.
* `get\_rank`: Provides the rank of the given taxon ID.
* `get\_mrca`: Finds the most recent common ancestor of a set of taxon IDs.
* `get\_downtorank\_id`: Provides the taxon ID of a higher rank, based on the input taxon ID and rank name.
*  `get\_lower\_from\_id`: Finds all lower taxon IDs for given taxon ID. Takes long as it needs to go through a large part of the files.
* `match\_id\_to\_mrca`: Checks if a given taxon ID belongs to a given mrca 



### Set up a run

#### Get started:

run from within the main folder:

* `python setup.py install`
* `pip install -r requirements.txt`

#### Translate ncbi names and IDs:

There is an `example.py` files in the main folder, which can easily be adapted for other purposes.
See the [PhylUp](https://github.com/mkandziora/PhylUp.git) package for an example on how to use it.    


### Make sure it runs
To check if the installation was successful and to initialize the download  of the taxonomy files from ncbi,
 a US government website, please run:

 `python3 ./tests/tests_setup.py`  # this will download the taxonomy files from ncbi, a US government website.
 
 `pytest tests/test_*`



### Acknowledgement

Thanks to Emily Jane McTavish who hired me as a postdoc during some time of development and the funding from NSF ABI grant \#1759846.

  
