#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:53:13 2017
Rosalind exercise "Rabbits and Recurrence Relations"
@author: evelina
"""
import sys
test = False

# Define the input
if test == True:
    n = int(input('n = '))
    k = int(input('k = '))
else:
    # Read the download file
    infile_name = sys.argv[1]
    infile = open(infile_name,'r')
    for line in infile:
        line = line.strip('\n')
        line = line.split()
        n = int(line[0])
        k = int(line[1])
    infile.close()

seq = [0, 1, 1]
for i in range(3, n+1):
    seq_i = seq[i-1] + k * seq[i-2]
    # alt: seq_i = seq[-1] + k * seq[-2]
    seq += [seq_i]
print(seq[n])