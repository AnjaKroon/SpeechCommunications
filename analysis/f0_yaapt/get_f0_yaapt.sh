# shell script to analyze pitch from mic signals and store as  *.yaapt txt files
#
# python script folder
P=/Users/anja/Desktop/ECSE523_TermProject/Term_Project/scripts
# data source
D=../../data/mic
#
for i in ${D}/*.wav
do
    echo $i
    x=`basename $i .wav`
    python3 ${P}/r_yaapt.py $i ${x}_f0.txt
done
