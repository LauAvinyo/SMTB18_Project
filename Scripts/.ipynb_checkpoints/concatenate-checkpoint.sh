for f in *.fasta; do
  o=${f%.*}                             # gets the code
  echo "$o"                             # prints the code
  mkdir "$o"                            # makes a directory with the name of the code
  cd "$o"                               # move to new directory
  python3 /mnt/c/Users/laura/SMTB18/SMTB18_Project/Scripts/03.getHomologous.py ../"$o"".blast"  # python script to retreive all seq
  cat *.fasta > "$o"".fst"              # concatenate everything
  rm *.fasta                            # remove single fastas
  cd ..
done