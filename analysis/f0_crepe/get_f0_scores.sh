# shell script to analyze pitch from mic signals and store as  *.crepe txt files
# loops over all the files in the data directory, runs the python script r_crepe.py
# r_crepe.py is the wrapper for the python code that was downloaded
# python script folder 

P=/Users/anja/Desktop/ECSE523_TermProject/Term_Project/scripts
# data source
D=.
R=../../data/f0_ref1
#
for i in ${D}/*_f0.txt
do
    #echo $i
    x=`basename $i .txt`
    echo $i $x
    python3 ${P}/score_pda.py ${R}/${x}.txt $i 
    mv score_pda.csv ${x}.csv
#run score pda with two arguments: reference file and test file
#make it run automatically
done


