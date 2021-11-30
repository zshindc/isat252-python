# Program that plots exercise 2 bonus
# Programmer: Zachary Shin
# matplotlib
# bonusexercise2.py

__author__= 'Zachary Shin'
import matplotlib.pyplot as plt
import math as math
def main():
    # generate 150 integers and store in list x
    x = [i * 0.1 for i in range(100)]
    y1 = [3*math.sin(2*math.pi*t) for t in x]
    y2 = [5 * math.exp(-t) * math.cos(2 * math.pi * t) for t in x]

    # optional - set size of plot
    fig = plt.figure(figsize=(5, 5), dpi=150)
	 
    #plot data
    plt.plot(x, y1, linestyle='solid', color='green', label="undamped wave")
    plt.plot(x, y2, linestyle="solid", color="red", label = "damped wave")
      
    #labels
    plt.xlabel("Time (seconds)")
    plt.ylabel("Intensity")
    plt.legend(loc="upper left")

    # title
    plt.title("Voice Identification and Sound Waves")
	 
    #optional -adjust plot
    plt.subplots_adjust(left=0.18)
	 
    #save plot-MUST do this FIRST before plt.show() in repl.it
    plt.savefig("shin_2_waves.png")
	 
    # show plot
    plt.show()

main()

