

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show()


'''
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
# https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
# https://www.youtube.com/watch?v=ZmYPzESC5YY&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF&index=16

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
plt.style.use('dark_background')

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)

# initialization function
def init():
	# creating an empty plot/frame
	line.set_data([], [])
	return line,

# lists to store x and y axis points
xdata, ydata = [], []

# animation function
def animate(i):
	# t is a parameter
	t = 0.1*i

	# x, y values to be plotted
	x = t*np.sin(t)
	y = t*np.cos(t)

	# appending new points to x, y axes points list
	xdata.append(x)
	ydata.append(y)
	line.set_data(xdata, ydata)
	return line,

# setting a title for the plot
plt.title('Creating a growing coil with matplotlib!')
# hiding the axis details
plt.axis('off')

# call the animator
anim = FuncAnimation(fig, animate, init_func=init,
							frames=500, interval=20, blit=True)

# save the animation as mp4 video file
anim.save('coil.gif',writer='imagemagick')

'''
