[![Build Status](https://travis-ci.com/blubbundbla/ncbiTAXONparser.svg?token=tcUKPEqrpyvHbPasst5i&branch=master)](https://travis-ci.com/blubbundbla/ncbiTAXONparser)

    
# ncbiTAXONparser

ncbiTAXONparser is a command-line tool written in python3 to translate names, ids and hierachical ranks for the ncbi taxonomy.


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

  