for f in *.pdb; do
    code=${f%.*} 
    echo $code
    echo $f
    python3 /home/a/SMTB18_Project/Scripts/08.getInterfaces.py $f 5 "$code"".interfaces"
done