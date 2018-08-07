for f in *.fasta; do
  o=${f%.*}
  echo "$o"
  mkdir "$o"
  cp "$f" "$o"
  python
  # cat *.fasta > "$o"".fst"
  #rm *.fasta
done