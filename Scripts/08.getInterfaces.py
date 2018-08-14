# Import libraries
import os
import sys
from Bio.PDB.PDBParser import PDBParser      # Parse the PDB



try:
    tresh = float(sys.argv[2])
except:
    print("ERROR: We need a distance from the surface and it must be the a float!")
    sys.exit(2)

try:
    outFile = open(sys.argv[3], 'w')
except:
    print("ERROR: Cannot open output file!")

parser = PDBParser(PERMISSIVE=1)
try:
    pdb_path = sys.argv[1]
    st = parser.get_structure('st', pdb_path)
except OSError:
    print ("ERROR: We cannot load the PDB! Did you provide a proper path?")
    sys.exit(2)

query = sys.argv[4]
agnts = sys.argv[5]

if len(st) > 1: # Checking for models
    print ("WARNING: Several Models found, using only first")

# Using Model 0 any way and the first chain
st = st[0]


aaSet = set(("Gly Pro Ala Val Leu Ile Met Cys Phe Tyr Trp His Lys Arg Gln Asn Glu Asp Ser Thr".upper()).split())
for chain in st.get_chains():
    if chain.id == query:
        stQuery = chain
    if chain.id == agnts:
        stAgnts = chain
        

qset = set()
aset = set()
for res in stQuery.get_residues():
    if res.get_resname() not in aaSet: continue
    if res.get_resname() == 'GLY':
        at1 = res['CA']
    else:
        at1 = res['CB']
        
    for res in stAgnts.get_residues():
        if res.get_resname() not in aaSet: continue
        if res.get_resname() == 'GLY':
            at2 = res['CA']
        else:
            at2 = res['CB']
        
        if at1 - at2 < tresh:
            qset.add((at1.get_parent().id[1], at1.get_parent().get_resname()))
            aset.add((at2.get_parent().id[1], at2.get_parent().get_resname()))
            
print('chain', 'pos', 'aa', sep='\t', file=outFile)
for res in qset:
    print(query, res[0], res[1], sep='\t', file=outFile)
    
for res in aset:
    print(agnts, res[0], res[1], sep='\t', file=outFile)