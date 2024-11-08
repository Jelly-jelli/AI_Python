"""
USE: python <PROGNAME> (options) 
OPTIONS:
    -h : print this help message and exit
    -d FILE : use FILE as data to create a new lexicon file
    -t FILE : apply lexicon to test data in FILE
"""
################################################################

import sys, re, getopt,nltk
from collections import defaultdict
import spacy


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
#{"run"↦→ { "verb" ↦→ 15, "noun" ↦→ 5 }, "'s" {"POS" -> 30}}

def count_pos_tag():
    term_postag_counts = {}
    remove_chars = [ ",","..","\\",'`','\'','%','-:','$','.']
    with open(input_file, "r") as file:
        content = file.read()
        for char in remove_chars:
            content = content.replace(char, "")
        #print ('len' , len(content))
        print(content)
        print(type(content))

    # Process each line
    for line in content:
        line = line.split()
        print(line)
        #if '/' in line:
        #Split the word and its tag
            #word, tag = line.split('/')
            #print(word)
            #print(tag)
        # Increment the count for the word and its tag
            #term_postag_counts[word][tag] += 1

        #Convert defaultdict to regular dict for better readability
        #term_postag_counts = {word: dict(tags) for word, tags in term_postag_counts.items()}

def main():
    count_pos_tag()

if __name__ == "__main__":
    main()