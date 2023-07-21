# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:18:49 2023

@author: Amar Doshi
"""


def PatternCount(Pattern, Genome):
    count = 0
    l = len(Pattern)

    for i in range(len(Genome) - l + 1):
        if Genome[i: i + l] == Pattern:
            count += 1

    return count


if __name__ == '__main__':
    
    print()

    # print(PatternCount('GCG', 'GCGCG'))

    print(PatternCount("TGT", "ACTGTACGATGATGTGTGTCAAAG"))
    