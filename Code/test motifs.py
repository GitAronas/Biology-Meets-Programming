# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:52:12 2023

@author: Amar Doshi
"""

from Motifs import *


m = ['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG']


def test_Count():
    c1 = {'A': [1, 2, 1, 0, 0, 2], 'C': [2, 1, 4, 2, 0, 0], 'G': [1, 1, 0, 2, 1, 1], 'T': [1, 1, 0, 1, 4, 2]}

    c2 = Count(m)

    print()
    print(c1)
    print(c2)

def test_Profile():
    d1 = {'A': [0.2, 0.4, 0.2, 0.0, 0.0, 0.4], 'C': [0.4, 0.2, 0.8, 0.4, 0.0, 0.0], 'G': [0.2, 0.2, 0.0, 0.4, 0.2, 0.2], 'T': [0.2, 0.2, 0.0, 0.2, 0.8, 0.4]}

    d2 = Profile(m)

    print()
    print(d1)
    print(d2)

def test_Consensus():
    c1 = 'CACCTA'

    c2 = Consensus(m)

    print()
    print(c1)
    print(c2)

def test_Score():
    s1 = 14

    s2 = Score(m)

    print()
    print(s1)
    print(s2)

def test_Pr():
    Text = 'ACGGGGATTACC'
    Profile = { 'A': [ 0.2 ,0.2 ,0.0 ,0.0 ,0.0 ,0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],'C': [ 0.1 ,0.6 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.4 ,0.1, 0.2, 0.4, 0.6], 'G': [ 0.0 ,0.0 ,1.0 ,1.0 ,0.9 ,0.9 ,0.1 ,0.0, 0.0 ,0.0 ,0.0, 0.0], 'T': [ 0.7 ,0.2 ,0.0 ,0.0 ,0.1 ,0.1 ,0.0, 0.5 ,0.8, 0.7, 0.3, 0.4]}

    p = Pr(Text, Profile)

    print()
    print(0.0008398080000000002)
    print(p)

def test_ProfileMostProbableKmer():
    k = 5
    text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    profile = {
        'A': [0.2, 0.2, 0.3, 0.2, 0.3],
        'C': [0.4, 0.3, 0.1, 0.5, 0.1],
        'G': [0.3, 0.3, 0.5, 0.2, 0.4],
        'T': [0.1, 0.2, 0.1, 0.1, 0.2]
        }

    p = ProfileMostProbableKmer(text, k, profile)

    print()
    print('CCGAG')
    print(p)

def test_GreedyMotifSearch():

    Dna = [
        "GGCGTTCAGGCA",
        "AAGAATCAGTCA",
        "CAAGGAGTTCGC",
        "CACGTCAATCAC",
        "CAATAATATTCG"
        ]

    g1 = '''
    CAG
    CAG
    CAA
    CAA
    CAA
    '''

    g2 = GreedyMotifSearch(Dna, 3, 5)

    print()
    print(g1)
    print(g2)


# test_GreedyMotifSearch()

def computeEntropy():
    # The entropy of a motif matrix is defined as the sum of the entropies of its columns.
    # Compute the entropy of the NF-κB motif matrix

    from math import log2

    profile = {
        'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
        'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
        'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
        }

    e = 0

    for v in profile.values():
        for i in v:
            if i > 0:
                e += i * log2(i)

    return -e

# print(computeEntropy())

'''
['GTTAGGGCCGGAAGT', 'CCGATCGGCATCACT', 'ACCGTCGATGTGCCC', 'GGGTCAGGTATATTT', 'GTGACCGACGTCCCC', 'CTGTTCGCCGGCAGC', 'CTGTTCGATATCACC', 'GTACATGTCCAGAGC', 'GCGATAGGTGAGATT', 'CTCATCGCTGTCATC']
64
'''

def test_Consensus1():
    m = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
     'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
     'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
     'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}

    c = Consensus(m)

    print()
    print(c)

# test_Consensus1()

def test_CountWithPseudocounts():
    c1 = {'A': [2, 3, 2, 1, 1, 3], 'C': [3, 2, 5, 3, 1, 1], 'G': [2, 2, 1, 3, 2, 2], 'T': [2, 2, 1, 2, 5, 3]}

    c2 = CountWithPseudocounts(m)

    print()
    print(c1)
    print(c2)

# test_CountWithPseudocounts()

def test_ProfileWithPseudocounts():
    p1 = {'A': [0.2222222222222222, 0.3333333333333333, 0.2222222222222222, 0.1111111111111111, 0.1111111111111111, 0.3333333333333333], 'C': [0.3333333333333333, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333, 0.1111111111111111, 0.1111111111111111], 'G': [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.3333333333333333, 0.2222222222222222, 0.2222222222222222], 'T': [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333]}

    p2 = ProfileWithPseudocounts(m)

    print()
    print(p1)
    print(p2)

# test_ProfileWithPseudocounts()

def test_GreedyMotifSearchWithPseudocounts():

    Dna = [
        "GGCGTTCAGGCA",
        "AAGAATCAGTCA",
        "CAAGGAGTTCGC",
        "CACGTCAATCAC",
        "CAATAATATTCG"
        ]

    g1 = '''
        TTC
        ATC
        TTC
        ATC
        TTC
        '''

    g2 = GreedyMotifSearchWithPseudocounts(Dna, 3, 5)

    print()
    print(g1)
    print(g2)

#test_GreedyMotifSearchWithPseudocounts()

def test_Motifs():
    DNA = ['TTACCTTAAC','GATGTCTGTC','ACGGCGTTAG','CCCTAACGAG','CGTCAGAGGT']
    Profile = { 'A': [0.8, 0.0, 0.0, 0.2 ],'C': [ 0.0, 0.6, 0.2, 0.0], 'G': [ 0.2 ,0.2 ,0.8, 0.0], 'T': [ 0.0, 0.2, 0.0, 0.8]}

    m1 = ['ACCT', 'ATGT', 'GCGT', 'ACGA', 'AGGT']

    m2 = Motifs(Profile, DNA)

    print()
    print(m1)
    print(m2)

# test_Motifs()

def test_RandomMotifs():
    DNA = ['TTACCTTAAC','GATGTCTGTC','ACGGCGTTAG','CCCTAACGAG','CGTCAGAGGT']

    m = RandomMotifs(DNA, 3, 5)

    print()
    print(m)

# test_RandomMotifs()

def test_Normalize():

    p1 = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
    p2 = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}

    p3 = Normalize(p1)

    print()
    print(p2)
    print(p3)

# test_Normalize()

def test_WeightedDie():
    p = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}

    k = WeightedDie(p)

    print()
    print(k)

# test_WeightedDie()

def test_ProfileGeneratedString():
    t = 'AAACCCAAACCC'
    p = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
    k = 2

    s = ProfileGeneratedString(t, p, k)

    print()
    print(s)

# test_ProfileGeneratedString()

def test_GibbsSampler():
    k = 8
    t = 5
    n = 100

    Dna = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
    ]

    m1 = ['AACGGCCA', 'AAGTGCCA', 'TAGTACCG', 'AAGTTTCA', 'ACGTGCAA']

    m2 = GibbsSampler(Dna, k, t, N)

    print()
    print(m1)
    print(m2)

test_GibbsSampler()