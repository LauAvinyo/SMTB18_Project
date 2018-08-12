for f in *.pdb; do
    code=${f%.*} 
    echo $code
    echo $f
    python3 /home/a/SMTB18_Project/Scripts/07.getSurfaceCore.py $f 5 "$code"".surf"
done