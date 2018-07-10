from Bio import AlignIO
import sys

prots = sys.argv[1:]
for input_name in prots:
    print(input_name)
    output_name = input_name[:-3]+'rel'
    print(output_name)

    input_handle = open(input_name, "rU")
    output_handle = open(output_name, "w")

    alignments = AlignIO.parse(input_handle, "clustal")
    AlignIO.write(alignments, output_handle, "phylip-relaxed")

    output_handle.close()
    input_handle.close()
