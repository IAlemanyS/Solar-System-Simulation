import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import animation
from IPython import display
from datetime import date, timedelta, datetime
import time

img = plt.imread("background.jpg")

N = 5
frames = 1096
lims = 0.3e9
w = np.loadtxt("resultado_todos_skip.txt", encoding = "cp1252")
n = len(w)
w = [[w[frames * i + k] for k in range(frames)] for i in range(int(n / frames))]

initdate = date(1800, 1, 1)

def animate(t):    
    ax = plt.axes()
    ax.clear()
    ax.set_xlim(-lims, lims)
    ax.set_ylim(-lims, lims)
    ax.imshow(img, extent=[-lims, lims, -lims, lims])
    #ax.set_facecolor("black")
    
    X = [w[i][t] for i in range(0, 3 * N, 3)]
    Y = [w[i + 1][t] for i in range(0, 3 * N, 3)]
    ax.scatter(X[0], Y[0], c = 'y', s = 15 * 69.55, animated = True)
    ax.scatter(X[1], Y[1], c = '#808c83', s = 40 * 0.24, animated = True)s
    ax.scatter(X[2], Y[2], c = 'orange', s = 40 * 0.60, animated = True)
    ax.scatter(X[3], Y[3], c = 'b', s = 40 * 0.63, animated = True)
    ax.scatter(X[4], Y[4], c = 'r', s = 40 * 0.34, animated = True)
    
    ax.text(lims - lims / 3.5, -lims + lims / 20, initdate + timedelta(days = 3 * t), fontsize = 12, color = 'white')
    
    return ax,

def init():
    return animate(0),

fig = plt.figure(figsize = (10, 10))
ani = animation.FuncAnimation(fig, animate, frames = range(1096), init_func = init, interval = 20)
ani.save("interiores-1096f-background.gif", fps = 30)

video = ani.to_html5_video()
html = display.HTML(video)
display.display(html)

#writervideo = animation.FFMpegWriter(fps = 30)
#ani.save("interiores-skip-300f.mp4", writer = writervideo)
plt.close()