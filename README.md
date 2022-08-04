# Title

## Overview:

## Running the project:

Note: python3 -> 'py' for Windows


- To install:
                        
            > git clone https://github.com/jgrindall/*
            > cd *
            > python3 -m venv venv
            > source venv/Scripts/activate
            > pip install -r requirements.txt


- To run on the command line (from the root folder):

            > python3 src/meme.py
            > python3 src/meme.py --path='_data/photos/cat/cat_1.jpg'
            > python3 src/meme.py --body='This is the body' --author='Someone'
            > python3 src/meme.py --path='_data/photos/dog/scooby_1/scooby_1.png' --body='This is the body' --author='Someone'
            


      

- To run some unit tests (currently just QuoteModel and Ingestor.py)

            > cd src
            > python3 -m doctest -v tests.txt


