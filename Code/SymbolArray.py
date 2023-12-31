# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:38:58 2023

@author: Amar Doshi
"""

from PatternCount import PatternCount


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    n2 = n // 2
    ExetendedGenome = Genome + Genome[: n2]

    for i in range(n):
        array[i] = PatternCount(symbol, ExetendedGenome[i: i + n2])

    return array


if __name__ == '__main__':

    # g = 'AAAAGGGG'
    # s = 'A'

    # print()
    # print('{0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}')
    # print(SymbolArray(g, s))

    # g = 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT'
    # s = 'CC'

    # '''
    # {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7, 7: 6, 8: 6, 9: 6, 10: 6, 11: 6, 12: 6, 13: 6, 14: 6, 15: 6, 16: 6, 17: 5, 18: 5, 19: 5, 20: 4, 21: 4, 22: 4, 23: 4, 24: 4, 25: 3, 26: 3, 27: 3, 28: 3, 29: 3, 30: 3, 31: 3, 32: 3, 33: 3, 34: 3, 35: 3, 36: 3, 37: 3, 38: 3, 39: 3, 40: 3, 41: 3, 42: 3, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 48: 2, 49: 2, 50: 3, 51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 2, 59: 2, 60: 2, 61: 2, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 4, 77: 4, 78: 4, 79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 5, 87: 5, 88: 5, 89: 6, 90: 6, 91: 6, 92: 6, 93: 6, 94: 7, 95: 7, 96: 7, 97: 7, 98: 7, 99: 7, 100: 7, 101: 7, 102: 7, 103: 7, 104: 6, 105: 6, 106: 6, 107: 7, 108: 7, 109: 7, 110: 7, 111: 7, 112: 8, 113: 8, 114: 8, 115: 8, 116: 7, 117: 7, 118: 7, 119: 7, 120: 7, 121: 7, 122: 7, 123: 7, 124: 7, 125: 7, 126: 7, 127: 8, 128: 7, 129: 7, 130: 7, 131: 7, 132: 7, 133: 7, 134: 7}
    # '''

    # c1 = {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7, 7: 6, 8: 6, 9: 6, 10: 6, 11: 6, 12: 6, 13: 6, 14: 6, 15: 6, 16: 6, 17: 5, 18: 5, 19: 5, 20: 4, 21: 4, 22: 4, 23: 4, 24: 4, 25: 3, 26: 3, 27: 3, 28: 3, 29: 3, 30: 3, 31: 3, 32: 3, 33: 3, 34: 3, 35: 3, 36: 3, 37: 3, 38: 3, 39: 3, 40: 3, 41: 3, 42: 3, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 48: 2, 49: 2, 50: 3, 51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 2, 59: 2, 60: 2, 61: 2, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 4, 77: 4, 78: 4, 79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 5, 87: 5, 88: 5, 89: 6, 90: 6, 91: 6, 92: 6, 93: 6, 94: 7, 95: 7, 96: 7, 97: 7, 98: 7, 99: 7, 100: 7, 101: 7, 102: 7, 103: 7, 104: 6, 105: 6, 106: 6, 107: 7, 108: 7, 109: 7, 110: 7, 111: 7, 112: 8, 113: 8, 114: 8, 115: 8, 116: 7, 117: 7, 118: 7, 119: 7, 120: 7, 121: 7, 122: 7, 123: 7, 124: 7, 125: 7, 126: 7, 127: 8, 128: 7, 129: 7, 130: 7, 131: 7, 132: 7, 133: 7, 134: 7}

    # c2 = SymbolArray(g, s)

    # print()
    # print(c2)

    # assert c2 == c1

    #TODO: Try running SymbolArray on your own computer with Genome equal to the E. coli genome and symbol equal to "C".

    '''
    If you attempted the previous exercise, then you may have wondered why the time limit was exceeded. The reason why is that SymbolArray is very slow.

    But wait, you may be wondering. Aren’t computers lightning-fast? Yet although computer speed has increased dramatically, even the fastest computer in the world cannot execute a program based on an inefficient algorithm.

    Why is SymbolArray inefficient? Its for loop makes n = len(Genome) iterations. Then, to compute PatternCount(symbol, ExtendedGenome[i:i+(n//2)]), we must compare symbol against n//2 symbols of ExtendedGenome. As a result, we require a total of n2//2 comparisons to execute SymbolArray(Genome, symbol). For a bacterial genome such as E. coli, which contains over 4.5 million nucleotides, we will need to execute over ten trillion symbol comparisons in order to generate a symbol array, which could take several days on a fast home computer operating several million comparisons per second.
    '''


    with open('E_coli.txt', "r") as f:
        Genome = f.read()

    symbol = 'C'

    a = SymbolArray(Genome, symbol)

    print(len(a))
