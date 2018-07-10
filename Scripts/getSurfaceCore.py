# Import libraries
import os
import sys
from Bio.PDB.PDBParser import PDBParser      # Parse the PDB
import Bio.PDB.ResidueDepth as ResidueDepth  # Get the distance from surface


# Read the inputs
if len(sys.argv) != 4:
    print("ERROR: We need a pdb and a distance from the surface!")
try:
    distanceSurface = float(sys.argv[2])
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

if len(st) > 1: # Checking for models
    print ("WARNING: Several Models found, using only first")

# Using Model 0 any way and the first chain
st = st[0]
st = tuple(st.get_chains())[0] # In case there is more than one line

residueID__depth = {}
resdepth=ResidueDepth(st)
for resInfo , depth in resdepth:
    residueID__depth[(resInfo.get_resname(), resInfo.get_full_id()[-1][1])] = depth[0]

print("aa", "pos", "surface", file=outFile, sep="\t")
for k in residueID__depth:
    if residueID__depth[k] < distanceSurface:
        print(k[0], k[1], 1, file=outFile, sep="\t")
    else:
        print(k[0], k[1], 0, file=outFile, sep="\t")
outFile.close()
