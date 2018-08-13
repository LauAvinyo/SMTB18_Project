from Bio.PDB import PDBParser, PDBIO
from Bio.PDB.Polypeptide import is_aa, three_to_one
import sys

path = sys.argv[1]
code = path[:-4]

io = PDBIO()
pdb = PDBParser().get_structure(code, path)

for chain in pdb.get_chains():
    io.set_structure(chain)
    io.save(pdb.get_id() + "_" + chain.get_id() + ".pdb")
    seq = list()
    out = open(code+"_"+chain.get_id()+'.fasta', 'w')
    for residue in chain:
        if is_aa(residue.get_resname(), standard=True):
            seq.append(three_to_one(residue.get_resname()))
        else:
            seq.append("X")
		 
		## This line is used to display the sequence from each chain
    print(">Chain_" + chain.get_id() + "\n" + str("".join(seq)), file=out)
    out.close()