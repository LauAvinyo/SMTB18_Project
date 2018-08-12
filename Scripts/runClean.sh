for f in *.alm; do
    code=${f%.*} 
    echo $code
    echo $f
    python3 ../../Scripts/04.cleanAligment.py $f "$code"".aln"
done