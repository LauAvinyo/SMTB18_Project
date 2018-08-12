for f in *.aln; do
    code=${f%.*} 
    echo $code
    echo $f
    python3 ../../Scripts/06.getRate.py $f "$code"".rate"
done