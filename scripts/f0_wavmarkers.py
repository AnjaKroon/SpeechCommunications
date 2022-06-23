#!/usr/bin/python3
#
# script to convert f0 txt file to wav file synchronized with mic wav file
#
import sys  #needed to read command line arguments
from os.path import exists as file_exists
import wave
import array as arr

# gets the command line parameters
# check if we have three arguments argv[0] which is the program name
# argv[1] which is the first argument representing the input file name
# argv[2] which is the second argument representing the output file name
scriptname = sys.argv[0]
# if not two arguments exit with a warning
if len(sys.argv) != 3 :
    print("Usage:", scriptname, "input_f0_txt  output_f0_wav")
    sys.exit()
# check if input file exist
else :
    file1 = sys.argv[1]
    file2 = sys.argv[2]
if not file_exists(file1) :
    print(scriptname, " - File not found: ", file1)
    sys.exit()
#
fs = 48000.     # fs in Hz
tframe = 0.01   # frame duration in s
#
framelength = int(tframe * fs + 0.5)
framespersec = int ( 1./tframe)
# create markers
#
print(scriptname + " - fs: " + str(fs))
print(scriptname + " - framelength: " + str(framelength))
print(scriptname + " - framespersec: " + str(framespersec))
#
f0_frame = arr.array('h', [0] * framelength)

with open(file1,'r') as f:
	data = f.readlines()
#
frames= len(data)
print("frames:", frames)
#
f= wave.open(file2,'wb')
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(fs)
#
# f0 values are scaled for display purposes since we plot them as a wavfile
# need to be careful not to exceed 32767
scalingfactor=10.
#
for i in range(0,frames):
    f0 = scalingfactor * float(data[i])
#    print(data[i],f0)
#
    for j in range(framelength):
        f0_frame[j]=int(f0)
    f.writeframes(f0_frame)

f.close()
#
