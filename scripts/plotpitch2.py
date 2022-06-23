#!/usr/bin/python3
# plotpitch2.py Updated: March 13, 2022
#
# plot two pitch contours from txt files
# imports
import matplotlib.pyplot as plt   # needed for plotting
import numpy as np                # needed for arrays
import sys                        # needed to read command line argument
from os.path import exists as file_exists
  
# shows the pitch_contour
def plotpitch(path: str):
    f0 = np.loadtxt(path)
    f0_rate = 100. # 100 Hz

    # to Plot the x-axis in seconds you need to get the sample rate
    # and divide by size of your signal to create
    # a Time Vector spaced linearly with the size of the input file
    time = np.linspace( 0, len(f0) / f0_rate, num = len(f0))

    # using matlplotlib to plot
    # creates a new figure
    plt.figure(1)

    # title of the plot
    plt.title(path)

    # label of x-axis
    plt.xlabel("Time")
    plt.ylabel("Pitch f0")
#    plt.ylim(0.,300.)

    # actual ploting but not showing until a call to plt.show is made
    plt.plot(time, f0)

if __name__ == "__main__":

    # gets the command line Value
    # check if we have three arguments argv[0] which is the program name
    # and argv[1] and argv[2] which represent the two file names
    # if not three arguments exit with a warning
    if len(sys.argv) != 3 :
        print("Usage:", sys.argv[0], "pitchfile1.txt pitchfile2.txt")
        sys.exit()
    else :
        path1 = sys.argv[1]
        path2 = sys.argv[2]
        if not file_exists(path1) :
            print("File not found: ", path1)
            sys.exit()
        elif not file_exists(path2) :
            print("File not found: ", path2)
            sys.exit()
        else:
            plt.subplot(211)
            plotpitch(path1)
            plt.subplots_adjust(hspace=0.5)
            plt.subplot(212)
            plotpitch(path2)
            plt.show()
