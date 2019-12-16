[![Build Status](https://travis-ci.com/blubbundbla/ncbiTAXONparser.svg?token=tcUKPEqrpyvHbPasst5i&branch=master)](https://travis-ci.com/blubbundbla/ncbiTAXONparser)

    
# ncbiTAXONparser

ncbiTAXONparser is a command-line tool written in python3 to translate names, ids and hierachical ranks for the ncbi taxonomy.


### Set up a run

#### Get started:

run from within the main folder:

* `python setup.py install`
* `pip install -r requirements.txt`

#### Translate ncbi names and IDs:

There is an example files in the main folder. Edit them for your purpose or use those function in your own workflows.
See the PhylUp package for an example on how to use it.    


### If you want to run some tests

run:

 `python3 ./tests/tests_setup.py`  # this will download the taxonomy files from ncbi, a US government website.
 
 `pytest tests/test_*`

  