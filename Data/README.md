The main sort of data (the proteins and their classification) comes from http://shmoo.weizmann.ac.il/elevy/3dcomplexV6/Download.cgi.
From this table (uploaded as well here in this folder) we can select the proteins we want. Note that in this list we only find human proteins, to construct 

### Downloading files using comand line

##### PDB files
`wget https://files.rcsb.org/download/XXXX.pdb`
And we have to ungz

##### Sequence files
`wget https://www.uniprot.org/uniprot/XXXXXX.fasta`

For example, if want to download deoxy human hemoglobine (PDB code: 1A3N, UniProt ID: P68871)

`wget https://files.rcsb.org/download/1A3N.pdb`

`wget ftp://ftp.wwpdb.org/pub/pdb/data/structures/all/pdb/pdb1A3N.ent.gz`

### More data:

##### EXAC
From the following database we can get how many mutations and so on there is for each gene. http://exac.broadinstitute.org/
Note that you have to browse using the Gene name, for instance, and we can get it from the Uniprot entrie.


