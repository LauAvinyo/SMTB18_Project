import sys
import pandas as pd
import wget


inputFile = sys.argv[1]
data = pd.read_table(inputFile)


for code in data['PDB']:
    url = "https://files.rcsb.org/download/"+code+".pdb"
    print(url)
    wget.download(url)
    
for code in data['UniID']:
    print(code)
    url = "https://www.uniprot.org/uniprot/"+code+".fasta"
    print(url)
    wget.download(url)