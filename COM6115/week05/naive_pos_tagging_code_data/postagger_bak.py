"""
USE: python <PROGNAME> (options) 
OPTIONS:
    -h : print this help message and exit
    -d FILE : use FILE as data to create a new lexicon file
    -t FILE : apply lexicon to test data in FILE
"""
################################################################

import sys, re, getopt,nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
from collections import defaultdict
import spacy
from spacy.cli import download
download("en_core_web_sm")

################################################################
# Command line options handling, and help

opts, args = getopt.getopt(sys.argv[1:], 'hd:t:')
opts = dict(opts)

def printHelp():
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print('-' * 60, help, '-' * 60, file=sys.stderr)
    sys.exit()
    
if '-h' in opts:
    printHelp()

if '-d' not in opts:
    print("\n** ERROR: must specify training data file (opt: -d FILE) **", file=sys.stderr)
    printHelp()

if len(args) > 0:
    print("\n** ERROR: no arg files - only options! **", file=sys.stderr)
    printHelp()


input_file = sys.argv[2]
################################################################
#{term ↦→ {postag ↦→ count}}
#{"run"↦→ { "verb" ↦→ 15, "noun" ↦→ 5 } }
def count_pos_tag():
    term_postag_counts = {}
    remove_chars = ["/", ",","..","\\",'`','\'','%','-:','$']
    with open(input_file, "r") as file:
        content = file.read()
        for char in remove_chars:
            content = content.replace(char, "")
        print ('len' , len(content))
        #print(content)

    term_pos_counts = defaultdict(lambda: defaultdict(int))

    # Load the spaCy model for English
    nlp = spacy.load("en_core_web_sm")
    nlp.max_length = 10000000
    # Tokenize and tag words with POS using nltk
    # tokens = nltk.word_tokenize(content)
    # tagged_words = nltk.pos_tag(tokens)

    # Process the text with spaCy
    doc = nlp(content)

    # Count occurrences of each word with each POS tag
    for token in doc:
        term_pos_counts[token.text][token.pos_] += 1

    # Count occurrences of each word with each POS tag
    #for word, pos in tagged_words:
    #    term_postag_counts[word][pos] += 1

    # To get the counts for a specific word, like "run":
    #word = "corporate"
    #print(f'Counts for "{word}":', dict(term_postag_counts[word]))
    print(term_pos_counts)


def main():
    count_pos_tag()


if __name__ == "__main__":
    main()