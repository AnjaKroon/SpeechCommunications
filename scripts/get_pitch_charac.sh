P=/Users/anja/Desktop/ECSE523_TermProject/Term_Project/scripts
# data source
D=.
#
for i in ${D}/*_f0.txt
do
    #echo $i
    x=`basename $i .txt`
    echo $i $x
    python3 ${P}/pitch_charac.py $i 
done