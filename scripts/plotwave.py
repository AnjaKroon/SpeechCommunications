#!/Users/peterkroon/venvs/dsp/bin/python3
# imports
import matplotlib.pyplot as plt   # needed for plotting
import numpy as np                # needed for arrays
import scipy.io.wavfile as wav    # needed for wav file read/write
import sys                        # needed to read command line argument
from os.path import exists as file_exists
import os.path
  
# shows the sound waves
def plotwaveform(path: str):
    
    f_rate,signal = wav.read(path)

    # to Plot the x-axis in seconds you need to get the sample rate
    # and divide by size of your signal to create
    # a Time Vector spaced linearly with the size of the audio file
    time = np.linspace( 0, len(signal) / f_rate, num = len(signal))

    # using matlplotlib to plot
    # creates a new figure
    plt.figure(1)

    # title of the plot
    file_name = os.path.basename(path)
    plt.title(file_name)
    #plt.title(path)

    # label of x-axis
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    # actual ploting
    plt.plot(time, signal)

    # shows the plot
    # in new window
    plt.show()

    # you can also save
    # the plot using
    # plt.savefig('filename')
if __name__ == "__main__":

    # gets the command line Value
    # check if we have two arguments argv[0] which is the program name
    # and argv[1] which is the first argument representing the file name
    # if not two arguments exit with a warning
    if len(sys.argv) != 2 :
        print("Usage:", sys.argv[0], "wavefile")
        sys.exit()
    else :
        path = sys.argv[1]
        if file_exists(path) :
            plotwaveform(path)
        else :
            print("File not found: ", path)
            sys.exit()
