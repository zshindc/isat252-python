# import matplotlib
import matplotlib.pyplot as plt
# generate some x-y data to plot
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
# plot the data
plt.plot(x,y)
plt.xlabel('x-values')
plt.ylabel('y-values')
# save the plot
plt.savefig('my_first_plot.png')
# show the plot
plt.show()