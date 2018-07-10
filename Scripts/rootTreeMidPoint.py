import sys
from ete3 import Tree

files = sys.argv[1:]
print(files)
for f in files:
    print(f)
    # Read the tree
    t = Tree(f)
    print(t)
    # Calculate the midpoint node
    R = t.get_midpoint_outgroup()
    # and set it as tree outgroup
    t.set_outgroup(R)
    # Write the tree
    t.write(format=1, outfile=f[:-3]+'net')
