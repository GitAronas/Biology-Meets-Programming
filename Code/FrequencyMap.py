# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 17:58:05 2023

@author: Amar Doshi
"""

def FrequencyMap(Text, k):
    dic = {}

    for i in range(len(Text) - k + 1):
        pattern = Text[i: i + k]
        dic[pattern] = dic.setdefault(pattern, 0) + 1

    return dic


if __name__ == '__main__':

    # {'CGA': 1, 'GAT': 1, 'ATA': 3, 'TAT': 2, 'ATC': 1, 'TCC': 1, 'CCA': 1, 'CAT': 1, 'TAG': 1}

    t = 'CGATATATCCATAG'
    
    t = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT" 
    
    k = 3

    d = FrequencyMap(t, k)

    print()
    print(d)
