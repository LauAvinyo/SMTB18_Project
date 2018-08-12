for f in *.alm; do
    code=${f%.*} 
    echo $code
    echo $f
    python3 /home/a/SMTB18_Project/Scripts/06.getRate.py $f "$code"".rate"
done