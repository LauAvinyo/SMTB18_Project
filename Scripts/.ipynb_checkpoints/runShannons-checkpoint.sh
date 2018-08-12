for f in *.aln; do
    code=${f%.*} 
    echo $code
    echo $f
    python3 ../../Scripts/05.getShannons.py $f "$code"".shannon"
done