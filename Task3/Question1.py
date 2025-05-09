
# Question 1: Word Counter
# Ask the user for a file name.
# Count and display the number of words in the file.
# Also, identify the most frequent word and how many times it appears.

import os
from collections import Counter
import string
pathh=input('please enter file path\n')
while pathh != 'q': 
    if os.path.exists(pathh):
        with open(file= pathh,mode='r') as fil:
            lines = fil.read()
            for p in string.punctuation:
                lines = lines.replace(p,'')
            words = lines.lower().split()  
            print(f'The number of words is : {len(words)}')
            word_counts = Counter(words)
            most_common = word_counts.most_common(1)
            print(f'The Most most frequent word is : "{most_common[0][0]}" \nits appeat {most_common[0][1]} times')
        break
    else:
        print('This file not exist.Please try again\n')
        pathh=input('please enter file path\n')
 