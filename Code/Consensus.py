# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:59:33 2023

@author: Amar Doshi
"""

# Nima Sarang submission
# Insert your Count(Motifs) function here.

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    matrix = Count(Motifs)
    consensus = ""
    for i in range(len(Motifs[0])):
        consensus += max(matrix, key=lambda e: matrix[e][i])
    return consensus


def Profile(Motifs):
    matrix = Count(Motifs)
    n = len(Motifs)

    for array in matrix.values():
        for i in range(len(array)):
            array[i] /= n
    return matrix


def Count(Motifs):
    row = len(Motifs)
    col = len(Motifs[0])
    count = {}

    for symbol in "ACGT":
        count[symbol] = [0] * col

    for i in range(row):
        for j in range(col):
            count[Motifs[i][j]][j] += 1
    return count


# Алексей Окунев submission
def most_frequent(List):
    return max(set(List), key = List.count)

def Consensus(Motifs):
    return ''.join([most_frequent([m[i] for m in Motifs]) for i in range(len(Motifs[0]))])
