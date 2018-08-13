for f in *.pdb; do
    code=${f%.*} 
    echo $code
    echo $f
    python3 ../../../Scripts/07.getSurfaceCore.py $f 2.5 "$code"".surf"
done