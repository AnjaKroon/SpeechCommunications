# shell script to convert ref_f0 files to r_f0
#
# data source
D=../f0_ref
#
for i in ${D}/*.txt
do
    echo $i
    x=`basename $i`
    # files are in DOS format and have <CR> at end of each line
    # use tr command to remove
    tr -d '\r' <$i >tmp1
    # we only need the first column 
    cut -f 1 -d ' ' tmp1 > ${x}
done
# clean up
rm -f tmp1
