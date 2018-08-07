import sys
import wget

inpFile = sys.argv[1]

with open(inpFile, 'r') as f:
    for line in f:
        l = line.strip()
        l = l.split('|')
        code = l[3].split('.')[0]
        url = "https://www.uniprot.org/uniprot/"+code+".fasta"
        print(url)
        wget.download(url)