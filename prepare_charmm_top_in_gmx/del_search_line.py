import sys
import re


in_file = sys.argv[1]

search_word = sys.argv[2]


with open(in_file) as f:

    for line in f:
        match = re.search(search_word, line)
    
        if not match:
            print(line, end='')

