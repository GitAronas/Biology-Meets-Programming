# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:13:29 2023

@author: Amar Doshi
"""

def HammingDistance(p, q):
    count = 0

    for j, k in zip(p, q):
        if k != j:
            count += 1

    return count


if __name__ == '__main__':

    # p = 'GGGCCGTTGGT'
    # q = 'GGACCGTTGAC'

    # c1 = 3

    # c2 = HammingDistance(p, q)

    # print()
    # print(c1)
    # print(c2)

    p = 'CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA'
    q = 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG'

    # c1 = 3

    c2 = HammingDistance(p, q)

    print()
    # print(c1)
    print(c2)
