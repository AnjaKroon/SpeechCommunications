#!/usr/bin/python3
# yaapt.py Updated: March 12, 2022
# wrapper for the hybrid time/frequency yaapt pitch predictor 
# Code from https://pypi.org/project/AMFM-decompy/
# http://bjbschmitt.github.io/AMFM_decompy/pYAAPT.html
#
# Input file is wav file
# Output file is txt file with pitch in Hz for each frame
#
import sys  #needed to read command line arguments
from os.path import exists as file_exists
import amfm_decompy.pYAAPT as pYAAPT
import amfm_decompy.basic_tools as basic

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
signal = basic.SignalObj(file1)
#
# YAAPT parameters and default settings
# ‘frame_length’ - length of each analysis frame (default: 35 ms)
# ‘frame_space’ - spacing between analysis frames (default: 10 ms)
# ‘f0_min’ - minimum pitch searched (default: 60 Hz)
# ‘f0_max’ - maximum pitch searched (default: 400 Hz)
# ‘fft_length’ - FFT length (default: 8192 samples)
# ‘bp_forder’ - order of band-pass filter (default: 150)
# ‘bp_low’ - low frequency of filter passband (default: 50 Hz)
# ‘bp_high’ - high frequency of filter passband (default: 1500 Hz)
# ‘nlfer_thresh1’ - NLFER (Normalized Low Frequency Energy Ratio) boundary for
#    voiced/unvoiced decisions (default: 0.75)
# ‘nlfer_thresh2’ - threshold for NLFER definitely unvoiced (default: 0.1)
# ‘shc_numharms’ - number of harmonics in SHC (Spectral Harmonics Correlation)
#    calculation (default: 3)
# ‘shc_window’ - SHC window length (default: 40 Hz)
# ‘shc_maxpeaks’ - maximum number of SHC peaks to be found (default: 4)
# ‘shc_pwidth’ - window width in SHC peak picking (default: 50 Hz)
# ‘shc_thresh1’ - threshold 1 for SHC peak picking (default: 5)
# ‘shc_thresh2’ - threshold 2 for SHC peak picking (default: 1.25)
# ‘f0_double’- pitch doubling decision threshold (default: 150 Hz)
# ‘f0_half’ - pitch halving decision threshold (default: 150 Hz)
# ‘dp5_k1’ - weight used in dynamic program (default: 11)
# ‘dec_factor’ - factor for signal resampling (default: 1)
# ‘nccf_thresh1’ - threshold for considering a peak in NCCF
#    (Normalized Cross Correlation Function) (default: 0.3)
# ‘nccf_thresh2’ - threshold for terminating search in NCCF (default: 0.9)
# ‘nccf_maxcands’ - maximum number of candidates found (default: 3)
# ‘nccf_pwidth’ - window width in NCCF peak picking (default: 5)
# ‘merit_boost’ - boost merit (default. 0.20)
# ‘merit_pivot’ - merit assigned to unvoiced candidates in definitely unvoiced
#     frames (default: 0.99)
# ‘merit_extra’ - merit assigned to extra candidates in reducing pitch 
#      doubling/halving errors (default: 0.4)
# ‘median_value’ - order of medial filter (default: 7)
# ‘dp_w1’ - DP (Dynamic Programming) weight factor for voiced-voiced transitions (default: 0.15)
# ‘dp_w2’ - DP weight factor for voiced-unvoiced or unvoiced-voiced transitions (default: 0.5)
# ‘dp_w3’ - DP weight factor of unvoiced-unvoiced transitions (default: 0.1)
# ‘dp_w4’ - Weight factor for local costs (default: 0.9)
# example to use different options
#pitch = pYAAPT.yaapt(signal, **{'f0_min' : 50.0, 'frame_length' : 25.0, 'frame_space' : 10.0})
#
# call YAAPT with default settings
pitch = pYAAPT.yaapt(signal)

# pitch is an object; the pitch values in Hz are the attribute samp_values
# the values are np.float
nframes=len(pitch.samp_values)
print("Number of frames:", nframes)
#
# write pitch to txt file
f = open(file2, "w")
for i in range(nframes):
    f.write('%s\n' % str(pitch.samp_values[i]))
f.close
