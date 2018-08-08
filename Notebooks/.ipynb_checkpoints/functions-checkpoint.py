def getShannon(alig, pos):
    from math import log
    count = {}
    for s in alig:
        aa = alig[s][pos]
        if aa in count:
            count[aa] += 1 # i++;
        else:
            count[aa] = 1
    
    nseq = len(alig)
    for s in count:
        count[s] /= nseq
    
    h = 0
    for w in count:
        h += count[w]*log(count[w])
    
    h = -h
    return h

def findGaps(alig,name):
    pos =[]
    seq = alig[name]
    for s in range(len(seq)):
        if seq[s] == "-":
            pos.append(s)
    return pos

def removePos(alig,dele):
    import numpy as np
    for name in alig:
        s = list(alig[name])
        s = np.array(s)
        s = np.delete(s, dele).tolist()
        s = ''.join(s)
        alig[name] = s
        
def countGapPos(alig, name):
    nSeq = len(alig)
    lSeq = len(alig[name])
    toDel=[]
    for i in range(lSeq):
        count = 0
        for x in alig:
            if alig[x][i] == "-":
                count += 1
        if count > nSeq*0.5:
            toDel.append(i)
    return toDel

def printDicAligFasta(alig, outFile):
    out = open(outFile, 'w')
    for name in alig:
        print('>'+name, file=out)
        print(alig[name], file=out)
    out.close()
    
def readAlig(file, form):
    from Bio import AlignIO
    alignment = AlignIO.read(open(file), form)
    alig= {}
    for s in alignment:
        if '|' in s.name:
            alig[s.name.split("|")[1]] = str(s.seq)    
        else: 
            alig[s.name] = str(s.seq)  
    return alig