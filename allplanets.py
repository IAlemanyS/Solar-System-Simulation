import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import animation

N = 9
frames = 3651
lims = 0.5e10
w = np.loadtxt("resultado_todos_100yrs.txt", encoding = "cp1252")
n = len(w)
w = [[w[frames * i + k] for k in range(frames)] for i in range(int(n / frames))]
def animate(t):
    ax = plt.axes()
    ax.clear()
    ax.set_xlim(-lims, lims)
    ax.set_ylim(-lims, lims)
    ax.set_facecolor("black")
    
    X = [w[i][t] for i in range(0, 3 * N, 3)]
    Y = [w[i + 1][t] for i in range(0, 3 * N, 3)]
    ax.scatter(X[0], Y[0], c = 'y', s = 0.5 * 69.55, animated = True)
    ax.scatter(X[1], Y[1], c = '#808c83', s = 10 * 0.24, animated = True)
    ax.scatter(X[2], Y[2], c = 'orange', s = 10 * 0.60, animated = True)
    ax.scatter(X[3], Y[3], c = 'b', s = 10 * 0.63, animated = True)
    ax.scatter(X[4], Y[4], c = 'r', s = 10 * 0.34, animated = True)
    ax.scatter(X[5], Y[5], c = '#fad98c', s = 10 * 7, animated = True)
    ax.scatter(X[6], Y[6], c = '#f2903a', s = 10 * 5.82, animated = True)
    ax.scatter(X[7], Y[7], c = 'cyan', s = 10 * 2.53, animated = True)
    ax.scatter(X[8], Y[8], c = 'blue', s = 10 * 2.46, animated = True)
    
    ax.text(lims - lims / 3.5, -lims + lims / 20, initdate + timedelta(days = 10 * t), fontsize = 12, color = 'white')
    
    return ax,

def init():
    return animate(0),

fig = plt.figure(figsize = (10, 10))
ani = animation.FuncAnimation(fig, animate, frames = range(3651), init_func = init, interval = 20)
ani.save("todos-3651f.gif", fps = 30)

video = ani.to_html5_video()
html = display.HTML(video)
display.display(html)