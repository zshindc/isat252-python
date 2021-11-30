# Program that plots exercise 1
# Programmer: Zachary Shin
# matplotlib
# exercise1.py

__author__ = 'Zachary Shin'
import matplotlib.pyplot as plt
import math as math

# could not find way to convert given materials to float for cos graph to generate

def main():
    # generate floats and store in list x
    x = [i * 0.01 for i in range(150)]
    # use list x to generate y-values
    y = [5 * math.exp(-t) * math.cos(2 * math.pi * t) for t in x]

    # optional - set size of plot
    fig = plt.figure(figsize=(5, 5), dpi=150)

    #plot data
    plt.plot(x, y, linestyle="solid", color="green")

    #labels
    plt.xlabel("Time (seconds)")
    plt.ylabel("Intensity")

    # title
    plt.title("Exponentially Decaying Sound Wave")

    #optional -adjust plot
    plt.subplots_adjust(left=0.18)

    #save plot-MUST do this FIRST before plt.show() in repl.it
    plt.savefig("shin_1_wave.png")

    # show plot
    plt.show()


main()
