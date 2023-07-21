# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:42:00 2023

@author: Amar Doshi
"""

def SkewArray(Genome):
    skew = [0] * (len(Genome) + 1)

    for i, c in enumerate(Genome):
        if c == 'A' or c == 'T':
            skew[i + 1] = skew[i]
        elif c == 'G':
            skew[i + 1] = skew[i] + 1
        elif c == 'C':
            skew[i + 1] = skew[i] - 1

    return skew


if __name__ == '__main__':

    # g = 'CATGGGCATCGGCCATACGCC'

    # s1 = '0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'

    # s2 = SkewArray(g)

    # print()
    # print(s1)
    # print(*s2)

    # g = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'

    # s1 = '0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'

    # s2 = SkewArray(g)

    # print()
    # # print(s1)
    # print(*s2)

    g = 'GATACACTTCCCGAGTAGGTACTG'

    s2 = SkewArray(g)

    print()
    # print(s1)
    print(*s2)
    print((min(s2)))
    