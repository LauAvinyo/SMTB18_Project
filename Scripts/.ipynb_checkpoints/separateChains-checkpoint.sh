for f in *.pdb; do
    code=${f%.*} 
    echo $code
    echo $f
    python3 ../../Scripts/separateChains.py $f 
done