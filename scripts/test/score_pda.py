#!/usr/bin/python3
# score_pda.py Updated: April 10, 2022
#
# script to score two pitch tracks
# first file is reference
# second file is pitch track to be scored
# scoring is based on method in
# A Comparative Performance Study of Several Pitch Detection Algorithms
# L Rabiner et al
# IEEE ASSP October 1976, pp399-418
#
# this scripts outputs the following additonal files
# score_pda.csv - results on one line file in csv format 
# score_pda_trace.txt - trace of voicing errors and gross pitch errors
# 0 = match between ref and test for voicing
# -1 = voiced to unvoiced error
# +1 = unvoiced to voiced error
# +2 = gross pitch error
#

import sys                      # needed to read command line argument
import numpy as np              # needed for standard deviation
from os.path import exists as file_exists

# gets the command line Value
# check if we have two arguments argv[0] which is the program name
# and argv[1] which is the first argument representing the file name
scriptname = sys.argv[0]
# if not two arguments exit with a warning
if len(sys.argv) != 3 :
    print("Usage:", scriptname, "ref_pitch_file test_pitch_file")
    sys.exit()
# check if file(s) exist
else :
    file1 = sys.argv[1]
    file2 = sys.argv[2]
if not file_exists(file1) :
    print(scriptname, " - File not found: ", file1)
    sys.exit()
if not file_exists(file2) :
    print(scriptname, " - File not found: ", file2)
    sys.exit()
#
#
fs=48000
framelength=480
#
print(scriptname, " - fs: ", fs)
print(scriptname, " - framelength: ", framelength)
#

with open(file1,'r') as f1:
	data1 = f1.readlines()
#
frames1= len(data1)
with open(file2,'r') as f2:
	data2 = f2.readlines()
#
frames2= len(data2)
frames=min(frames1, frames2)
if frames1 != frames2 :
    print(scriptname, " - framecounts do not match:", frames1, frames2)
    print(scriptname, " - using smaller one", frames)
    if abs(frames1 - frames2) > 20 :
        print(scriptname, " - frame count mismatch too large")
        sys.exit()

#
MAXTGROSS=0.01  #max abs delta to exceed to be counted as cross error
unvoiced_frames=0
voiced_frames=0
unvoiced_voiced_errors=0
voiced_unvoiced_errors=0
gross_pitch_errors=0
fine_pitch_errors=0
# create empty array to store pitch differences
t_err_array = np.zeros(frames)
# create empty array to store error trace
# zero if voicing matches
# +1 if unvoiced_voiced error
# -1 if voiced_unvoiced error
# +2 if gross pitch error
err_trace = np.zeros(frames)

for i in range(0,frames):
    f_ref=float(data1[i])
    f_tst=float(data2[i])
#    print(i,f_ref, f_tst)
    if f_ref == f_tst and f_ref == 0.0 :
        unvoiced_frames = unvoiced_frames + 1
    elif f_ref == 0.0 and f_tst != 0.0 :
        unvoiced_voiced_errors = unvoiced_voiced_errors +1
        err_trace[i] = 1
    elif f_ref != 0.0 and f_tst == 0.0 :
        voiced_unvoiced_errors = voiced_unvoiced_errors +1
        err_trace[i] = -1
    else:
        # both f_ref and f_tst have pitch
        voiced_frames = voiced_frames + 1
# NEED TO DECIDE IF WE WANT TO COMPARE FREQUENCY OR TIME
# RABINER PAPER USES TIME
# to be able to compare results let's use time
        t_ref = 1/f_ref
        t_tst = 1/f_tst
        t_err =  t_ref- t_tst
        if abs(t_err) >= MAXTGROSS :
            gross_pitch_errors = gross_pitch_errors +1
            err_trace[i] = 2
        else :
        # to compute std recursively is possible (Welford algorithm) 
        # but here we just write all the difference data to an array first
        # and compute it later
            t_err_array[fine_pitch_errors] = t_err
            fine_pitch_errors = fine_pitch_errors + 1
#
mean=np.mean(t_err_array[0:fine_pitch_errors])
std=np.std(t_err_array[0:fine_pitch_errors])
#
# summarize results
print("File name                :", file2)
print("Total frames compared    :", frames)
print("Unvoiced frames          :", unvoiced_frames)
print("Unvoiced/Voiced errors   :", unvoiced_voiced_errors)
print("Voiced/Unvoiced errors   :", voiced_unvoiced_errors)
print("Voiced frames            :", voiced_frames)
print("Gross pitch errors       :", gross_pitch_errors)
print("Fine pitch errors        :", fine_pitch_errors)
print("Fine pitch errors (mean) :", "%3.8f"%mean)
print("Fine pitch errors (stdev):", "%3.8f"%std)
f1.close()
f2.close()
#
# write data to one line in csv file
#
csvline=[str(file2),str(frames),str(unvoiced_frames),str(unvoiced_voiced_errors),str(voiced_unvoiced_errors),str(voiced_frames), str(gross_pitch_errors), str(fine_pitch_errors),str(mean),str(std)]
#
f3 = open('score_pda.csv','w')
for line in csvline:
    f3.write(line)
    f3.write(',')
f3.write('\n')
f3.close()
#
# write trace to txt file
f4 = open('score_pda_trace.txt', "w")
for i in range(frames):
        f4.write('%s\n' % str(err_trace[i]))
f4.close
