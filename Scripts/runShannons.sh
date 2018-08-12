for f in *.alm; do
    code=${f%.*} 
    echo $code
    echo $f
    python3 /home/a/SMTB18_Project/Scripts/05.getShannons.py $f "$code"".shannon"
done