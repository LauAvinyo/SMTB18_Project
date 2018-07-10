The pipeline goes as follow:

1. Get all the data. 
2. Multiple alignment: with T-Coffee.
3. Trees: with PHYLIP, note that the you the data must bw formated.
4. Structure analysis - what is the surface, what is the core: We need to get the PDB.
    - Divide the protein in chains (Ask Baldo for the script)
    - Use MSMS to divide the protein in core vs surface. You have to choose the ratio,eg, the water one
5. Integration of trees and structural data.
    - There is a python notebook that merges everything.
    - However the following analyses are not done.
6. Comparison of the results for different groups of proteins. Interpretation of the results.
