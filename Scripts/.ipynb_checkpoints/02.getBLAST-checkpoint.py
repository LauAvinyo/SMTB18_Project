import sys
import pandas as pd

inputFile = sys.argv[1]
data = pd.read_table(inputFile)

taxa = {
    'Scer': 'Saccharomycetales',
    'Hsap':'Mammalia',
    'Ecoli':'Enterobacteriales',
    'Celg':'nematodes'
}

outName = 'blast_'+inputFile[:-3] + 'sh'
outFile = open(outName, 'w')
for a in data.index:
    spc = data.iloc[a]['Species']
    uni = data.iloc[a]['UniID']
    print("blastp -query "+data.iloc[a]['UniID']+".fasta -db nr -remote \
    -entrez_query "+ taxa[data.iloc[a]['Species']]+"[Organism]  -outfmt '6 sseqid' -out "+data.iloc[a]['UniID']+".blast", file=outFile)
outFile.close()