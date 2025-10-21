import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d
import numpy as np



# Define x and y values along with a grid of them globally for all functions
x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.5)
x, y = np.meshgrid(x, y)

# define functions 
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
    ax.plot_surface(a, b, Z)


    # second subplot
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    Z = np.ma.masked_where((Z > 10) | (Z < -10), Z)
    ax.contourf(a,b,Z, 200)

    # Allow for potential plotting of extra points
    # Useful to show multiple extrema points if present
    ax.plot([xlim], [ylim], [limval], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    if extra is not None:
        ax.plot(extra[0], extra[1], extra[2] , markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    if extra1 is not None:
        ax.plot(extra1[0], extra1[1], extra1[2] , markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    
    # Set labels for graph and display
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    plt.show()

# Establish loop to allow for selective viewing of limit plots
seeLim = input("Would you like to see a limit graph? y/n ")
while seeLim == "y":
    choice = int(input("Which limit would you like to see? "))
    if choice == 1:
        # limit one
        print("Limit value = 1/2")
        makePlot(f(x,y),1,1,0.5,x,y)
    elif choice == 2:
        # limit two
        print("This limit does not exist")
        makePlot(g(x,y), 0, 0, 0, x, y)
    elif choice ==3:
        # limit three
        print("Limit value = -1/6")
        makePlot(h(x,y), 0,-1, -1/6, x, y)
    seeLim = input("Would you like to see another? y/n ")



# Display Extrema plot one
input("Second part: Press Enter to continue")
print("This graph has a local maxima at (1,2)")
makePlot(f1(x,y),1,2,4,x,y)

# Display extrema plot two
input("Press Enter to continue:")
print("This graph has two local maxima and one local minima \n Local maxima occur at both (0,1) and (0,-1) \n Local minima occurs at (0,0)")
makePlot(g1(x,y),0,0,0,x,y,[0,1,1.1036],[0,-1,1.1036])