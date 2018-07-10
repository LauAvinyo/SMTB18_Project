for f in *.fas; do
  echo "$f"
  o=${f%.*}
  t_coffee "$f" > "$o"".tcf";
done
