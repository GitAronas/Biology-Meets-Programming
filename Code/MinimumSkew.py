# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:38:12 2023

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


def MinimumSkew(Genome):
    positions = []

    skew = SkewArray(Genome)

    minval = min(skew)

    for i, val in enumerate(skew):
        if val == minval:
            positions.append(i)

    return positions


if __name__ == '__main__':

    # g = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'

    # p1 = '11 24'

    # p2 = MinimumSkew(g)

    # print()
    # print(p1)
    # print(*p2)

    g = 'GATACACTTCCCGAGTAGGTACTG'

    # p1 = '11 24'

    p2 = MinimumSkew(g)

    print()
    # print(p1)
    print(*p2)
