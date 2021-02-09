#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:32:46 2020

@author: Kate
"""


import csv
from itertools import zip_longest

def listify(file):
    f = open(file, 'r')
    
    tokens = []
    LIDs = []
  
    sentence_tokens = []
    sentence_lids = []
    
    for line in f:  # token level
#        print(line)

        if line != '\n':
            columns = line.split('\t')  # isolate columns
            
        if line == '\n':
            # add sentences to tokens/LIDs
            tokens.append(sentence_tokens)
            LIDs.append(sentence_lids)
            
            # reset lists for next sentence
            sentence_tokens = []
            sentence_lids = []
                
#            print(columns)
        
        # add romanised words to sent_tokens, LIDs to sent_lids
        else:
            sentence_tokens.append(columns[1])
            sentence_lids.append(columns[-2])

    # create big list of [romanised words] and [LIDs]
    big_ls = []
    big_ls.append(tokens)
    big_ls.append(LIDs)
    
#    print(big_ls[0][:10])
#    print(big_ls[1][:10])
    
#    for sentence in big_ls[:10]:
#        print(sentence) [[[s1], [s2]], [[lid1], [lid2]]]
    
    export_data = zip_longest(*big_ls, fillvalue = '')
    
    with open(file + '.csv', 'w') as new_file:
        wr = csv.writer(new_file)
        wr.writerow(['tokens', 'LID'])
        wr.writerows(export_data)
#        for ls in big_ls:
#            wr.writerow(ls)
    new_file.close()