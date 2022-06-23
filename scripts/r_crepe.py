#!/usr/bin/python3
# r_crepe.py Updated: March 12, 2022
# wrapper for the neural net crepe pitch predictor 
#https://pypi.org/project/crepe/
#
# Input file is wav file
# Output file is txt file with pitch in Hz for each frame
#
import sys  #needed to read command line arguments
from os.path import exists as file_exists
import crepe
from scipy.io import wavfile

# gets the command line parameters
# check if three arguments argv[0] which is the program name
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
# call crepe
fs, audio = wavfile.read(file1)
# use all the possible arguments
# this use insight is from code inspection of core.py
#Output is
#time, frequency, confidence
#0.00, 424.24, 0.42
#0.01, 422.42, 0.84
#...
#time is a timestamp in seconds,
#frequency is the estimated frequency in Hz
#confidence is a value between 0 and 1 indicating the model's voicing confidence
#(i.e.  confidence in the presence of a pitch for every frame).
#Input parameters
#model-capacity= {tiny,small,medium,large,full}
#String specifying the model capacity; smaller models
#are faster to compute, but may yield less accurate pitch estimation
#viterbi=True         perform Viterbi decoding to smooth the pitch curve
#center=False    Don't pad the signal, meaning frames will begin at
#their timestamp instead of being centered around their
#timestamp (which is the default center=True). CAUTION: setting
#this option can result in CREPE's output being
#misaligned with respect to the output of other audio
#processing tools and is generally not recommended.
#step-size=STEP_SIZE The step size in milliseconds for running pitch estimation
#The default is 10 ms. Which is what is needed for the pitch detector from Graz.
#
time, frequency, confidence, activation = crepe.predict(audio, fs, model_capacity='full', viterbi=True,center=False, step_size=10, verbose=0)

#now writing out the pitch value from crepe
nframes=len(time)
print("Number of frames:", nframes)
#
# all pitch values with Confidence < CONFIDENCE will be set to 0.0
# write pitch to txt file
CONFIDENCE = 0.5 
f = open(file2, "w")
for i in range(nframes):
    if confidence[i] < CONFIDENCE :
        f.write('0.0\n') #if confidence less than 0.5 when voiced, the write out a pitch value of 0
    else :
        f.write('%s\n' % str(frequency[i])) #if confidence is greater than 0.5 when voiced, then write out the pitch value
f.close
