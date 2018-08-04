# Homomers vs Heteromers!
Proteins works in complexes. This complexes can be:
  - Homomers: all subunits come from the same gene
  - Heteromers: not all subunits come from the same gene
  
It is known that both types of complexes are important for the functionality and stability of proteins. However, it remains to know why some of them are homo and some of them are hetero. It could be that there are some differences between them! For instance, in the evolution of the sequences. So, this is what we are going to do.
We will grap some homomers and some heteromers from different species (homo sapiens, saccharomyces cerevisiae, escherichia coli and caenorhabditis elegans). Then, we'll look for homologous proteins using simple blast againts swiss prot. 
Then we will the rate of evolution for each of the proteins. To do so, we will use protein and DNA data:

### Protein data:
  1. We will transfrom DNA to protein sequences
  2. We will align all the sequences per protein
  3. We will get an idea of each site conservation using Shannon entropy  
  4. We will investigate how to get rates of evolution for each site using already written code
  5. We will analyse the structures of the proteins to see what is the core and what is in the interface.
  6. We will merge all data and try to figure out if there is any difference


The following papers is a good inspiration for this project: the [paper](https://f1000research.com/articles/6-1845/v1) its [github](https://github.com/clauswilke/proteinER).

# How to install everything in linux

### T-Coffee
The simplest way is using the apt package manager:
`sudo apt-get install t-coffee`
Type the password and agree.

### PHYLIP
The easiest way to run is downloading the C sources in a know folder (better if it is in a program folder or something like that).
1. Move wherever you think is confortable to have the code and executaples and type:
`mkdir phylip`

2. Then you have to Download the C-sources from the PHYLIP website:
`wget http://evolution.gs.washington.edu/phylip/download/phylip-3.697.tar.gz`

3. Untar the sources: 
`tar -zxvf phylip-3.697.tar.gz`

4. Move to the src files:
`cd phylip-3.697/src/`

5. Compile the pograms:
`make -f Makefile.unx install`

And that is all you have the executables done!
Remember that for running them you have to call them from the exe folder or ./name_exe if ou are in the same folder than the execulatble. However, you can add the folder in your path.

### BioPython
To install it with pip:
`python3.6 -m pip install biopython`

You can do it from the source code but it is rather difficult. Also, if you do not have pip you can install it using: `sudo apt-get install python3-pip`

### MSMS
1. Move to our desired installing folder. eg. msms folder in the same folder of before.

2. Get the executables:
`wget http://mgltools.scripps.edu/downloads/tars/releases/MSMSRELEASE/REL2.6.1/msms_i86_64Linux2_2.6.1.tar.gz`

3. Untar the folder:
`tar -zxvf msms_i86_64Linux2_2.6.1.tar.gz`
Now, you have a folder with the executables. You can run the programs from here. However, we want to use them from BioPython so we need to have msms in the bin folder.

4. Move to the bin folder:
`cd /usr/local/bin`

5. Copy the executable and change its name to msms:
`sudo cp ~/installing/msms/msms.x86_64Linux2.2.6.1 msms`

Done!
