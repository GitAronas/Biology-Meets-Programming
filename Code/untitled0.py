# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 17:01:04 2023

@author: Amar Doshi
"""


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


# Find the most frequent 2-mer of "GATCCAGATCCCCATAC".

def FrequentWords(Text, PatternLength):
    dic = {}

    for i in range(len(Text) - PatternLength + 1):
        pattern = Text[i: i + PatternLength]
        dic[pattern] = dic.setdefault(pattern, 0) + 1

    return dic


if __name__ == '__main__':

    t = "GATCCAGATCCCCATAC"
    t = "CGATATATCCATAG"

    l = 3

    d = FrequentWords(t, l)

    maxval = max(d.values())

    maxvals = [k for k, v in d.items() if v == maxval]

    print()
    print(maxvals)
    print()

    s = sorted(d.items(), key=lambda x: x[1], reverse=True)

    for k, v in s:
        print(k, v)

    # ds = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

    # for k, v in ds.items():
    #     print(k, v)
