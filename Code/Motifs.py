# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:47:11 2023

@author: Amar Doshi
"""
from random import randint, choices


def GibbsSampler(Dna, k, t, N):
    pass


def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}

    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)

    probabilities = Normalize(probabilities)

    return WeightedDie(probabilities)


def WeightedDie(Probabilities):
    return choices(list(Probabilities.keys()), weights=list(Probabilities.values()), k=1)[0]


def Normalize(Probabilities):
    t = sum(Probabilities.values())

    return {k: v / t for k, v in Probabilities.items()}


def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)

        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


def RandomMotifs(Dna, k, t):
    motifs = []

    for strand in Dna:
        i = randint(0, len(strand) - k)
        motifs.append(strand[i: i + k])

    return motifs


def Motifs(Profile, Dna):
    # k = 4
    k = len(Profile['A'])
    motifs = []

    for strand in Dna:
        mx = -1

        for i in range(len(strand) - k + 1):
            s = strand[i: i + k]
            t = sum(Profile[c][i] for i, c in enumerate(s))

            if t > mx:
                mx = t
                motif = s

        motifs.append(motif)

    return motifs


def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []

    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))

        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs

    return BestMotifs


def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4
    k = len(Motifs[0])

    profile = CountWithPseudocounts(Motifs)

    for v in profile.values():
        for i in range(k):
            v[i] /= t

    return profile


def CountWithPseudocounts(Motifs):
    A, C, G, T = 'A', 'C', 'G', 'T'
    count = {A:[], C:[], G:[], T:[]}

    for t in zip(*Motifs):
        count[A].append(t.count(A) + 1)
        count[C].append(t.count(C) + 1)
        count[G].append(t.count(G) + 1)
        count[T].append(t.count(T) + 1)

    return count


def Count(Motifs):
    A, C, G, T = 'A', 'C', 'G', 'T'
    count = {A:[], C:[], G:[], T:[]}

    for t in zip(*Motifs):
        count[A].append(t.count(A))
        count[C].append(t.count(C))
        count[G].append(t.count(G))
        count[T].append(t.count(T))

    return count


def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    profile = Count(Motifs)

    for v in profile.values():
        for i in range(k):
            v[i] /= t

    return profile


def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)

    consensus = ''

    for j in range(k):
        m = 0
        frequentsymbol = ''

        for symbol in 'ACGT':
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentsymbol = symbol

        consensus += frequentsymbol

    return consensus


def Score(Motifs):
    count = 0
    c = Consensus(Motifs)

    for i in range(len(c)):
        for motif in Motifs:
            if motif[i] != c[i]:
                count += 1

    return count


def Pr(Text, Profile):
    p = 1

    for i, c in enumerate(Text):
        p *= Profile[c][i]

    return p


def ProfileMostProbableKmer(text, k, profile):
    m = -1
    c = ''

    for i in range(len(text) - k + 1):
        t = text[i: i + k]
        p = Pr(t, profile)

        if p > m:
            m = p
            c = t

    return c


def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []

    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))

        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs

    return BestMotifs
