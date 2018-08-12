from functions import *
from Bio import AlignIO
import matplotlib.pyplot as plt
import sys

alp=list("ACDEFGHIKLMNPQRSTVWY")

charge = {
    'positive' : set(('R','H', 'K')),
    'negative' : set(('D', 'E')),
    'neutral'  : set(('A', 'N', 'C', 'Q', 'G', 'I', 'L', 'M', 
                     'F', 'P', 'S', 'T', 'W', 'Y', 'U'))
    }

polarity = {
    'polar'  : set(('R', 'N', 'D', 'C', 'Q', 'E', 
                   'G', 'H', 'K', 'S', 'T', 'Y')),
    'apolar' : set(('A', 'I', 'L', 'M',
                  'F', 'F', 'W', 'V'))
}

polarityVolume = {
    'special'      : set('C',),
    'neutralSmall' : set(('A', 'G', 'P', 'S', 'T')),
    'polarSmall'   : set(('N', 'D', 'Q', 'E')),
    'polarLarge'   : set(('R', 'H', 'K')),
    'apolarSmall'  : set(('I', 'L', 'M', 'V')),
    'apolarLarge'  : set(('F', 'W', 'Y'))
}

aa_charact = {}
for i in alp:
    for k in charge:
        if i in charge[k]:
            c = k
    for k in polarity:
        if i in polarity[k]:
            p = k
    for k in polarityVolume:
        if i in polarityVolume[k]:
            v = k
    aa_charact[i] = (c, p, k)
    
inputFile  = sys.argv[1]
outputFile = sys.argv[2]
code = inputFile.split('.')[0]

alig = readAlig(inputFile, 'fasta')
query = code

lSeq = len(alig[query])
nSeq = len(alig)

alp
listSubs = []
for i in range(len(alp)):
    for j in range(i, len(alp)):
        listSubs.append((alp[i], alp[j]))

listSubs = tuple(listSubs)

subsDic = {}
for x in range(lSeq):
    subsDic[x]= {}
    for y in listSubs:
        subsDic[x][y] = 0
        
sequences = tuple(alig[i] for i in alig)
for x in range(lSeq):
    for y in range(nSeq):
        for z in range(y+1, nSeq):
            aa1 = sequences[y][x]
            aa2 = sequences[z][x]
            if aa1 not in alp or aa2 not in alp: continue
            sub = (min(aa1,aa2), max(aa1,aa2))
            subsDic[x][sub] += 1

conservative = set()
for aa1 in polarity['polar']:
    for aa2 in polarity['polar']:
        subs = (min(aa1,aa2), max(aa1,aa2))
        conservative.add(subs)

for aa3 in polarity['apolar']:
    for aa4 in polarity['apolar']:
        subs1 = (min(aa3,aa4), max(aa3,aa4))
        conservative.add(subs1)
        
radical = set()
for aa5 in polarity['polar']:
    for aa6 in polarity['apolar']:
        subs2 = (min(aa5,aa2), max(aa1,aa6))
        radical.add(subs2)

consRad = {} 
for p in range(lSeq):
    consRad[p] = [0, 0]
    for s in listSubs:
        if s in conservative:
            consRad[p][0] += subsDic[p][s]
        else: # if s in radical
            consRad[p][1] += subsDic[p][s]
        
ratio = []

for x in range(lSeq):
    if consRad[x][1] == 0:
        r = 0
    else: 
        r = consRad[x][0]/consRad[x][1]   
    ratio.append(r)
    
mean = sum(ratio)/ len(ratio)

norm1 = list(((x-mean)/mean) for x in ratio)

out=open(outputFile, "w")
print('cons', 'rad', 'ratio', 'norm', file=out, sep='\t')
for x in range(len(ratio)):
    print(consRad[x][0], consRad[x][1], ratio[x], norm1[x], file=out, sep='\t')
out.close()
