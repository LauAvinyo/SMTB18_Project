import sys
import pandas as pd
import wget
from Bio import Entrez
Entrez.email= "laura.avino@alum.esci.upf.edu"

inputFile = sys.argv[1]

with open(inputFile, 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split("|")
        if line[2] == 'pdb':
            url = "https://www.rcsb.org/pdb/download/downloadFastaFiles.do?structureIdList="+line[3]+"&compressionType=uncompressed"
            wget.download(url)
        else:
            code = line[3]
            handle = Entrez.efetch(db="protein", id=code,rettype="fasta", retmode="text")
            ut = open(code+".fasta", 'w')
            print(handle.read(), file=ut)
            ut.close()