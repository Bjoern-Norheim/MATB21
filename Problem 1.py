import matplotlib.pyplot as plt 
import matplotlib
from mpl_toolkits.mplot3d import axes3d
import numpy as np

plt.style.use('_mpl-gallery')

# Define Globally for all functions
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)

def f(X,Y):
    return (X**2 - X*Y)/(X**2 - Y**2)



# Limit 1.1
def makePlot(function, xlim, ylim, limval):
    Z = function
    # make window wide enough to fit multiple graphs
    fig = plt.figure(figsize=plt.figaspect(0.5))

    # first plot
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2)

    # second subplot
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.contourf(X,Y,Z, 200)

    ax.plot([xlim], [ylim], [limval], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    plt.show()


makePlot(f(X,Y),1,1,0.5)
input("Press enter to continue")




