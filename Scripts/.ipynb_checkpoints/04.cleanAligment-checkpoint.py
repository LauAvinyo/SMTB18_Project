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

toDel = findGaps(alig, code)
removePos(alig, toDel)

printDicAligFasta(alig, outputFile)