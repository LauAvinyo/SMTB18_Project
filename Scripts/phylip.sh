for f in *.inp; do
  echo "$f"
  "$1" < "$f" >> "$2"
done
