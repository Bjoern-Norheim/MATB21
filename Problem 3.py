import matplotlib.pyplot as plt 
import matplotlib
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from scipy.optimize import fsolve

plt.style.use('_mpl-gallery')

# Define Globally for all functions
X = np.arange(-10, 10, 0.5)
Y = np.arange(-10, 10, 0.5)
X, Y = np.meshgrid(X, Y)
Z = np.zeros_like(X)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

def f(Z,X,Y):
    return X + 2*Y + Z + np.e**Z - 1




def makePlot(function):
   for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i,j] = fsolve(f,0,args=(X[i,j], Y[i,j]))[0]

    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2)

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")

    plt.show()



makePlot(f(X,Y,Z))

# git add .
# git commit -m "Your message here"
# git push 