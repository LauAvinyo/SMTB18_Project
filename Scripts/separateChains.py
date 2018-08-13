from Bio.PDB import PDBParser, PDBIO
import sys

path = sys.argv[1]

io = PDBIO()
pdb = PDBParser().get_structure("st", path)

for chain in pdb.get_chains():
    io.set_structure(chain)
    io.save(pdb.get_id() + "_" + chain.get_id() + ".pdb")


	for residue in chain:
		    ## The test below checks if the amino acid
		    ## is one of the 20 standard amino acids
		    ## Some proteins have "UNK" or "XXX", or other symbols
		    ## for missing or unknown residues
		    if is_aa(residue.get_resname(), standard=True):
		        seq.append(three_to_one(residue.get_resname()))
		    else:
		        seq.append("X")
		 
		## This line is used to display the sequence from each chain
		 
		print(">Chain_" + chainID + "\n" + str("".join(seq)))
		 
		## The next two lines create a sequence object/record
		## It might be useful if you want to do something with the sequence later
		 
		myProt = Seq(str(''.join(seq)), IUPAC.protein)
		seqObj = SeqRecord(myProt, id=chainID, name="", description="")
