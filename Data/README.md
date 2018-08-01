The main sort of data (the proteins and their classification) comes from http://shmoo.weizmann.ac.il/elevy/3dcomplexV6/Download.cgi.
From this table (uploaded as well here in this folder) we can select the proteins we want.

### Downloading using comand line

##### PDB files
`wget ftp://ftp.wwpdb.org/pub/pdb/data/structures/all/pdb/pdbXXXX.ent.gz`
And we have to ungz

##### Sequence files
`wget https://www.uniprot.org/uniprot/XXXXXX.fasta`

For example, if want to download deoxy human hemoglobine (PDB code: 1A3N, UniProt ID: P68871)
`wget ftp://ftp.wwpdb.org/pub/pdb/data/structures/all/pdb/pdb1A3N.ent.gz`

