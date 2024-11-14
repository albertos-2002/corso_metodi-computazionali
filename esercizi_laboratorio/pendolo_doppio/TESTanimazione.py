import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

"""
dt intervallo temporale
t numero di grame in forma di lista 
coord matrice 4 righe frame colonne
"""

def animazione(dt, t, coord, trail_length=50):
    fig, ax = plt.subplots()
    
    # Initialize line and trail data arrays
    l1x = np.zeros((2), dtype=np.float64)
    l1y = np.zeros((2), dtype=np.float64)
    history2x = np.zeros((trail_length))
    history2y = np.zeros((trail_length))
    history3x = np.zeros((trail_length))
    history3y = np.zeros((trail_length))
    
    # Create line segments and points
    l1x[0] = 0
    l1y[0] = 0
    l1x[1] = coord[0, 0]
    l1y[1] = coord[1, 0]
    line1 = ax.plot(l1x, l1y)[0]

    l2x = np.zeros((2), dtype=np.float64)
    l2y = np.zeros((2), dtype=np.float64)
    l2x[0] = coord[0, 0]
    l2y[0] = coord[1, 0]
    l2x[1] = coord[2, 0]
    l2y[1] = coord[3, 0]
    line2 = ax.plot(l2x, l2y)[0]

    trail2 = ax.plot(history2x, history2y, 'b-', alpha=0.5)[0]
    trail3 = ax.plot(history3x, history3y, 'g-', alpha=0.5)[0]

    disc1, = ax.plot([], [], 'ro', markersize=10)
    disc2, = ax.plot([], [], 'bo', markersize=10)
    disc3, = ax.plot([], [], 'go', markersize=10)

    ax.set(xlim=[-4, 4], ylim=[-4, 4], xlabel='X [m]', ylabel='Y [m]')

    # Update function for each frame
    def update(frame):
        l1x[1] = coord[0, frame]
        l1y[1] = coord[1, frame]
        l2x[0] = coord[0, frame]
        l2y[0] = coord[1, frame]
        l2x[1] = coord[2, frame]
        l2y[1] = coord[3, frame]
        line1.set_xdata(l1x)
        line1.set_ydata(l1y)
        line2.set_xdata(l2x)
        line2.set_ydata(l2y)

        disc1.set_data(0, 0)
        disc2.set_data(coord[0, frame], coord[1, frame])
        disc3.set_data(coord[2, frame], coord[3, frame])

        # Update trails for disc2 and disc3
        frame_in = max(frame - trail_length, 0)
        for ifr in range(frame - frame_in):
            history2x[ifr] = coord[0, ifr + frame_in]
            history2y[ifr] = coord[1, ifr + frame_in]
            history3x[ifr] = coord[2, ifr + frame_in]
            history3y[ifr] = coord[3, ifr + frame_in]

        trail2.set_data(history2x, history2y)
        trail3.set_data(history3x, history3y)

        return line1, line2, disc1, disc2, disc3, trail2, trail3

    ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=int(dt * 1000), blit=True)
    plt.show()

# Parameters for the test
dt = 0.1  # Frame interval time in seconds
t = np.linspace(0, 10, 100)  # Time array with 100 time steps
coord = np.random.rand(4, 100) * 8 - 4  # Random coordinates within the plot range [-4, 4]

# Execute the animation function
animazione(dt, t, coord)
