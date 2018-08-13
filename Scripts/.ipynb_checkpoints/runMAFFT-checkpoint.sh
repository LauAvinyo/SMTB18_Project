for f in *.fst; do
    code=${f%.*} 
    echo $code
    echo $f
    "/usr/bin/mafft"  --auto --reorder "$f" > "$code"".alm"  
done