# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:14:22 2023

@author: Amar Doshi
"""

def HammingDistance(p, q):
    count = 0

    for j, k in zip(p, q):
        if k != j:
            count += 1

    return count


def ApproximatePatternCount(Pattern, Text, d):
    d += 1
    count = 0
    l = len(Pattern)

    for i in range(len(Text) - l + 1):
        if HammingDistance(Text[i: i + l], Pattern) < d:
            count += 1

    return count


if __name__ == '__main__':

    p = 'GAGG'
    t = 'TTTAGAGCCTTCAGAGG'
    d = 2

    c1 = 4

    c2 = ApproximatePatternCount(p, t, d)

    print()
    print(c1)
    print(c2)
