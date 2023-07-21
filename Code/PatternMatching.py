# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:29:28 2023

@author: Amar Doshi
"""


def PatternMatching(Pattern, Genome):
    l = len(Pattern)

    return [i for i in range(len(Genome) - l + 1) if Genome[i: i + l] == Pattern]


if __name__ == '__main__':
    p = 'ATAT'

    print()
    print(p)
    print()

    print(PatternMatching(p, 'GATATATGCATATACTT'))
