# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 18:17:16 2023

@author: Amar Doshi
"""

# nucleotides A and T are complements of each other, as are C and G.

BASEPAIRS = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}


def Reverse(Pattern):
    return Pattern[::-1]


def Complement(Pattern):
    return ''.join(BASEPAIRS[c] for c in Pattern.upper())


def ReverseComplement(Pattern):   
    return Complement(Reverse(Pattern))


if __name__ == '__main__':

    p = 'AAAACCCGGT'
    
    p = "GATTACA"

    print()
    print(p)
    print(ReverseComplement(p))
