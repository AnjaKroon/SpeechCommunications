#!/usr/bin/python3
# yin.py Updated: March 13, 2022
# wrapper for the time yin pitch predictor 
# https://librosa.org/doc/0.9.1/generated/librosa.pyin.html#librosa.pyin
#
# Input file is wav file
# Output file is txt file with pitch in Hz for each frame
#
import sys  #needed to read command line arguments
from os.path import exists as file_exists
import librosa

# gets the command line parameters
# check if we have three arguments argv[0] which is the program name
# argv[1] which is the first argument representing the input file name
# argv[2] which is the second argument representing the output file name
scriptname = sys.argv[0]
# if not two arguments exit with a warning
if len(sys.argv) != 3 :
    print("Usage:", scriptname, "input_wav_file  output_pitch_file")
    sys.exit()
# check if input file exist
else :
    file1 = sys.argv[1]
    file2 = sys.argv[2]
if not file_exists(file1) :
    print(scriptname, " - File not found: ", file1)
    sys.exit()
# we need to use the wav IO routine from the package 
# to get it in the proper object format
y, fs = librosa.load(file1)


# call YIN 
HP_LENGTH=int(fs * 0.010)  # 10 ms
pitch, voiced, confidence = librosa.pyin(y,fmin=50, fmax=500, sr=fs, center=False, hop_length=HP_LENGTH)

# pitch is an object; the pitch values in Hz are the attribute samp_values
# the values are np.float
nframes=len(pitch)
print("Number of frames:", nframes)
#
# write pitch to txt file
f = open(file2, "w")
for i in range(nframes):
    if voiced[i] :
        f.write('%s\n' % str(pitch[i]))
    else :
        f.write('0.0\n')
f.close
