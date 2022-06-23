# shell script to analyze pitch from mic signals and store as  *.crepe txt files
# loops over all the files in the data directory, runs the python script r_crepe.py
# r_crepe.py is the wrapper for the python code that was downloaded
# python script folder 
P=/Users/anja/Desktop/ECSE523_TermProject/Term_Project/scripts
# data source
D=../../data/mic
#
for i in ${D}/mic_M09*.wav
do
    echo $i
    x=`basename $i .wav`
    python3 ${P}/r_crepe_1.py $i ${x}_f0.txt
done
