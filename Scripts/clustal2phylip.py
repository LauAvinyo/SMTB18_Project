from Bio import AlignIO
import sys

# It recieves a list of pritein aligments 
# It changes the format of the the aligment
prots = sys.argv[1:]
for input_name in prots:
    print(input_name)
    output_name = input_name[:-3]+'phy'
    print(output_name)

    input_handle = open(input_name, "rU")
    output_handle = open(output_name, "w")

    alignments = AlignIO.parse(input_handle, "clustal")
    AlignIO.write(alignments, output_handle, "phylip")

    output_handle.close()
    input_handle.close()
