# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:17:24 2023

@author: Amar Doshi
"""

'''
Now imagine that you are trying to find ori in a newly sequenced bacterial genome. Searching for “clumps” of "ATGATCAAG"/"CTTGATCAT" or "CCTACCACC"/"GGTGGTAGG" is unlikely to help, since this new genome may use a completely different hidden message! Before we lose all hope, let’s change our computational focus: instead of finding clumps of a specific k-mer, let’s try to find every k-mer that forms a clump in the genome. Hopefully, the locations of these clumps will shed light on the location of ori.

Our plan is to slide a window of fixed length L along the genome, looking for a region where a k-mer appears several times in short succession. The parameter value L = 500 reflects the typical length of ori in bacterial genomes.

We think of a k-mer as a “clump” if it appears many times within a short interval of the genome. More formally, given integers L and t, a k-mer Pattern forms an (L, t)-clump inside a (longer) string Genome if there is an interval of Genome of length L in which this k-mer appears at least t times. (This definition assumes that the k-mer completely fits within the interval.) For example, "TGCA" forms a (25, 3)-clump in the following Genome:

gatcagcataagggtccCTGCAATGCATGACAAGCCTGCAGTtgttttac


From our previous examples of ori regions, "ATGATCAAG" forms a (500, 3)-clump in the Vibrio cholerae genome, and "CCTACCACC" forms a (500, 3)-clump in the Thermotoga petrophila genome. We are now ready to formulate the following problem.

Clump Finding Problem:
 Find patterns forming clumps in a string.
     Input: A string Genome, and integers k, L, and t.

     Output: All distinct k-mers forming (L, t)-clumps in Genome.

Don’t worry about writing an algorithm to solve the Clump Finding Problem; we have done it for you. When we used this algorithm to look for clumps in the Escherichia coli (E. coli) genome, the workhorse of bacterial genomics, we found hundreds of different 9-mers forming (500, 3)-clumps in this genome. It is absolutely unclear which of these 9-mers might represent a DnaA box in the bacterium’s ori region.
'''


# gatcagcataagggtccCTGCAATGCATGACAAGCCTGCAGTtgttttac