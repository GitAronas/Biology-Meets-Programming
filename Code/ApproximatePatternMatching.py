# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:22:29 2023

@author: Amar Doshi
"""

def HammingDistance(p, q):
    count = 0

    for j, k in zip(p, q):
        if k != j:
            count += 1

    return count


def ApproximatePatternMatching(Text, Pattern, d):
    l = len(Pattern)
    d += 1

    return [i for i in range(len(Text) - l + 1) if HammingDistance(Text[i: i + l], Pattern) < d]


if __name__ == '__main__':

    p = 'ATTCTGGA'
    t = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
    d = 3

    p1 = '6 7 26 27'

    p2 = ApproximatePatternMatching(t, p, d)

    print()
    print(p1)
    print(*p2)
