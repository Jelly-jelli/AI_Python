"""\
------------------------------------------------------------
USE: python <PROGNAME> (options) file1...fileN
OPTIONS:
    -h : print this help message
    -s FILE : use stoplist file FILE
    -p : use Porter stemming (default: no stemming)
    -b : use BINARY weights (default: count weighting)
    CMD : python compare.py -s stop_list.txt NEWS/news01.txt NEWS/news02.txt
------------------------------------------------------------\
"""

import sys, re, getopt
import glob
from nltk.stem import PorterStemmer

opts, args = getopt.getopt(sys.argv[1:], 'hs:pbI:')
opts = dict(opts)

##############################
# HELP option

if '-h' in opts:
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print(help, file=sys.stderr)
    sys.exit()

##############################
# Identify input files, when "-I" option used

if '-I' in opts:
    filenames = glob.glob(opts['-I'])
else:
    filenames = args

# Check if filenames are being found 
# (comment out after checking)
print('INPUT-FILES:', filenames, file=sys.stderr)

##############################
# STOPLIST option

stops = set()
if '-s' in opts:
    with open(opts['-s'], 'r') as stop_fs:
        for line in stop_fs :
            stops.add(line.strip())
            
##############################
# Stemming function

stemmer = PorterStemmer().stem

def stem_word(word):
    return stemmer(word)

##############################
# COUNT-WORDS function. 
# Takes 2 inputs: 1= FILE-NAME, 2= stoplist
# Returns a dictionary of word counts

def count_words(filename, stops):
    word_list = []
    counts = {}
    # Define the regex pattern for words
    word_pattern = re.compile(r'\b[a-zA-Z]+\b')

    # Open the file for reading
    with open(filename, 'r') as file:
        for line in file:
            # Find all words in the line
            words = word_pattern.findall(line)
            # Process the words (print them in this example)
            for word in words:
                print(word.lower())
                word_list.append(word.lower())

    for word in word_list:
        # Count word not in stop list
        if word not in stops:
            count = word_list.count(word)
            counts[word] = count
    #print(counts)

    return counts

##############################
# Compute counts for individual documents

docs = [ ]

for infile in filenames:
    docs.append(count_words(infile, stops))

##############################
# Compute similarity score for document pair
# Inputs are dictionaries of counts for each doc
# Returns similarity score
# docs is list of dictionary

def jaccard(doc1, doc2):
    # Calculate sensitive
    # Merge 2 dict --> z = {**x, **y}
    all_list = {**doc1, **doc2}


    #print('DOC1 : ' , doc1)
    keys_list_doc1 = set(doc1.keys())
    keys_list_doc2 = set(doc2.keys())
    print('key1' , keys_list_doc1)

    # intersection of two sets
    intersection = len(keys_list_doc1.intersection(keys_list_doc2))
    # Unions of two sets
    union = len(keys_list_doc1.union(keys_list_doc2))

    #Calculate sensitive
    print('union all doc : ' , all_list)


    return intersection / union

##############################
# Compute scores for all document pairs

results = {}
for i in range(len(docs)-1):
    for j in range(i+1, len(docs)):        
        pair_name = '%s <> %s' % (filenames[i], filenames[j])
        results[pair_name] = jaccard(docs[i], docs[j])

##############################
# Sort, and print top N results

top_N = 20

pairs = list(results) # DUMMY CODE LINE 
# Replace with code to sort results based on scores.
# Have only results for highest "top_N" scores printed.

# Printing
c = 0
for pair in pairs:
    c += 1
    print('[%d] %s = %.3f' % (c, pair, results[pair]), file=sys.stdout)

##############################

