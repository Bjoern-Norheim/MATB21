import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d
import numpy as np

plt.style.use('_mpl-gallery')

# Define Globally for all functions
x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.5)
x, y = np.meshgrid(x, y)

def f(X,Y):
    return (X**2 - X*Y)/(X**2 - Y**2)

def g(X,Y):
    return (X**2 + Y**2)/(X**2 + X*Y + Y**2)

def h(X,Y):
    return (np.sin(X + X*Y) - X - X*Y)/(X**3 * (Y+1)**3)
def f1(X,Y):
    return 8*X*Y - 4*Y*X**2 - 2*X*Y**2 + (X**2)*Y**2
def g1(X,Y):
    return (X**2+3*Y**2)*(np.e)**(-X**2-Y**2)
                                  

# Limit 1.1
def makePlot(function, xlim, ylim, limval, a, b, extra=None, extra1=None):
    Z = function
    # make window wide enough to fit multiple graphs
    fig = plt.figure(figsize=plt.figaspect(0.5))

    # first plot
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    Z = np.ma.masked_where((Z > 10) | (Z < -10), Z)
    # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(a, b, Z)


    # second subplot
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    Z = np.ma.masked_where((Z > 10) | (Z < -10), Z)
    ax.contourf(a,b,Z, 200)


    ax.plot([xlim], [ylim], [limval], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    if extra is not None:
        ax.plot(extra[0], extra[1], extra[2] , markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    if extra1 is not None:
        ax.plot(extra1[0], extra1[1], extra1[2] , markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    plt.show()


makePlot(f(x,y),1,1,0.5,x,y)
input("Press enter to continue")
makePlot(g(x,y), 0, 0, 0, x, y)
input("Press enter to continue")
makePlot(h(x,y), 0,-1, -1/6, x, y)

x1 = np.arange(0,2,0.5)
y1 = np.arange(0,4,0.5)
x1, y1 = np.meshgrid(x1, y1)

input("Second part: Press Enter to continue")
makePlot(f1(x,y),1,2,4,x,y)
input("Press Enter to continue:")
makePlot(g1(x,y),0,0,0,x,y,[0,1,1.1036],[0,-1,1.1036])