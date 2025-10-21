import matplotlib.pyplot as plt 
import matplotlib
from mpl_toolkits.mplot3d import axes3d
import numpy as np

# Define Globally for all functions
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
# Create figure; done globally so we can plot gradient points on the same figures
fig = plt.figure(figsize=plt.figaspect(0.5))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

def makePlot(function):
    Z = function

    # Plot the surfaces
    ax1.plot_surface(X, Y, Z, vmin=Z.min() * 2)
    ax2.contourf(X,Y,Z,20,alpha=0.35)


    ax1.set_xlabel("X axis")
    ax1.set_ylabel("Y axis")
    ax1.set_zlabel("Z axis")
    gradientDescent(0,0, 'r')
    gradientDescent(1/5,-4,'b')
    plt.show()


def gradientDescent(x1, y1, color):
    i = 0
    a = 0.01
    xk = np.array([x1,y1])

    # create an arry of function values and compute the gradient
    x = np.linspace(-5,5,100)
    y = np.linspace(-5,5,100)
    X, Y = np.meshgrid(x, y)

    # Evaluate the function at the various x,y values
    F = (X**2 + Y - 11)**2 + (X + Y**2 - 7)**2

    
    # Step size for finite differences
    h = 1e-3

    # Compute and arry of gradient values
    # Gradient equations taken from problem 2
    dF_dx = (f(X + h, Y) - f(X, Y)) / h
    dF_dy = (f(X, Y + h) - f(X, Y)) / h 
    
    

    for i in range(0,20):
        # Finds the (x,y) point on the function grid which is closest to your current continusou position after the step
        ix = np.argmin(np.abs(x - xk[0]))
        iy = np.argmin(np.abs(y - xk[1]))

        # plot current step
        ax2.plot([xk[0]], [xk[1]], [f(xk[0], xk[1])], markerfacecolor=color, markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
        
        # calculate gradient value and apply gradient descent algorithm
        grad = np.array([dF_dx[iy, ix], dF_dy[iy, ix]])
        xk1 = xk - a * grad
        xk = xk1
        


def f(X,Y):
    return (X**2 + Y - 11)**2 + (X + Y**2 - 7)**2


makePlot(f(X,Y))

