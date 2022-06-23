#looking at the pitch contour and summarizing pitch range
#get the minimuma and maximum average value
#make a histogram of the pitch distribution
#In the plot package there is a plt.hist routine; example
# setting the ranges and no. of intervals range = (50, 500)   #minimum and maximum pitch bins = 50
# plotting a histogram plt.hist(ages, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8)
#examine what kinds of erros are made
import sys                      # needed to read command line argument
import numpy as np              # needed for standard deviation
from os.path import exists as file_exists
import matplotlib
import matplotlib.pyplot as plt

import os.path

#would need to take one file in
scriptname = sys.argv[0]
# if not one argument exit with a warning
if len(sys.argv) != 2 :
    print("Usage:", scriptname, "pitch file in txt form to characterize")
    sys.exit()
else:
    file1 = sys.argv[1]
if not file_exists(file1):
    print(scriptname, " - File not found: ", file1)
    sys.exit()
#read lines in txt file
with open(file1,'r') as f1:
    data1 = f1.readlines()
#number of frames/number of lines in the txt file

frames1 = len(data1)
j = 0
pitchArr = np.empty(frames1)
#use max and min of python
#use histogram function
#make a numpy array with all zeros removed
for i in range(frames1):
   fdata = float(data1[i])
   if fdata != 0.0:
       #print('adding', fdata)
       pitchArr[j] = fdata
       j = j+1
# print(pitchArr) #so now we have a numpy array
min_val = np.min(pitchArr[0:j])
median_val = np.median(pitchArr[0:j])
max_val = np.max(pitchArr[0:j])

print('min value:           ', min_val)
print('median value:        ', median_val)
print('max value:           ', max_val)

#for comparison, say the minimum pitch is 50 and maximum pitch is 500
bins = 70
range_ofnums = (50,500)
plt.hist(pitchArr, bins, range_ofnums, color = 'green', histtype = 'bar', rwidth = 0.8)
plt.xlabel('Pitch [Hz]')
plt.ylabel('# of Occurrences')
file_name = os.path.basename(file1)
plt.title(file_name)
file_noext = os.path.splitext(file_name)
plt.savefig(file_noext[0]+'.png')


#CONTINUE
#file name, pitch values, min, median, max
csvline=[str(file_name),str(j),str(min_val),str(median_val),str(max_val)]

f3 = open(file_noext[0]+'.csv','w')
for line in csvline:
    f3.write(line)
    f3.write(',')
f3.write('\n')
f3.close()




