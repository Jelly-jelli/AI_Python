"""
USE: python <PROGNAME> (options) WORDLIST-FILE INPUT-FILE OUTPUT-FILE
OPTIONS:
    -h : print this help message and exit
"""
################################################################
# COMMAND TO RUN
#  /usr/bin/python3 /Users/jellymacbook/PycharmProjects/Python_COM6115/week03/chinese_segmentation_resources/chinese_segmentation_STARTER_CODE.py week03/chinese_segmentation_resources/chinesetrad_wordlist.utf8 week03/chinese_segmentation_resources/chinesetext.utf8 MYRESULTS.utf8

import sys
import binascii
################################################################

MAXWORDLEN = 5

################################################################
# Command line options handling, and help

def print_help():
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print('-' * 60, help, '-' * 60, file=sys.stderr)
    sys.exit(0)
    
if '-h' in sys.argv or len(sys.argv) != 4:
    print_help()

word_list_file = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

################################################################

# PARTS TO COMPLETE: 

################################################################
# READ CHINESE WORD LIST
# Read words from Chinese word list file, and store in 
# a suitable data structure (e.g. a set)

with open(word_list_file, "r", encoding = "utf-8") as myfile:
    #word_set = set([line.rstrip('\n') for line in myfile])
    wordset = set([line.strip() for line in myfile])
    #print(len(word_set))
    print("Final set : ", wordset)


with open(input_file, 'rb') as f:
    filecontent = f.read()
    chunk1 = filecontent[:11]
    #print(chunk1)
    # Decode character back to chinese
    #print(chunk1.decode('utf8'))

################################################################
# FUNCTION TO PROCESS ONE SENTENCE
# Sentence provided as a string. Result returned as a list of strings 

def segment_bak (sent, wordset):
    # main loop
    # Begin with 0
    i = 0
    # length equal to max which is 5
    # MAXWORDLEN = 5
    word = []
    length = len(MAXWORDLEN)
    while length > 1:
        position = sent[i] + length-1
        print('word : ', position)
        if position in wordset:
            print('YES:')
            #update new position
            position = position + length
        else:
            print('NO:')
            length -= 1

    if length == 1:
        position = sent[i]
        print('char' , position)

    return list(sent)

def segment(sentence, wordset):
    words = []
    sentlen = len(sentence)
    current = 0
    while current < sentlen:
        maxlen = min(sentlen - current, MAXWORDLEN)
        for i in range(maxlen, 0, -1):
            candidate = sentence[current:current+i]
            if i == 1 or candidate in wordset:
                words.append(candidate)
                current += i
                break
    return words

################################################################
# MAIN LOOP
# Read each line from input file, segment, and print to output file
def main():
    print("python main function")
with open(input_file, encoding = "utf8") as text_in, \
     open(output_file, "w", encoding = "utf8") as text_out:
    for line in text_in:
        words = segment(line.strip(), wordset)
        print(' '.join(words), file = text_out)



if __name__ == '__main__':
    main()
################################################################

