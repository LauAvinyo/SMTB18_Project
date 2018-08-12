from Bio import AlignIO
from math import log
import matplotlib.pyplot as plt
import numpy as np
from functions import *
import sys

inputFile  = sys.argv[1]
outputFile = sys.argv[2]
code = inputFile.split('.')[0]

alig = readAlig(inputFile, 'fasta')
length = len(alig[code])

# Get the Shannons entropy by position
hs = []
for pos in range(0, length):
    hs.append(getShannon(alig, pos))
    
    
outFile = open(outputFile, 'w')
print('pos', 'entropy', file=outFile, sep='\t')
for i, h in enumerate(hs):
    print(i+1, h, file=outFile, sep='\t')
outFile.close()
    