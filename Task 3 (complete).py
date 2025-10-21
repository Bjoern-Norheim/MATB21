import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from scipy.optimize import fsolve

#part 1

def F(x,y,z):
    return x + 2*y +z + np.exp(2*z)-1

#create rectangular domain [-0.5,0.5]x[-0.5,0.5]
x = np.linspace(-0.5, 0.5, 101)
y = np.linspace(-0.5, 0.5, 101)
X, Y = np.meshgrid(x, y)

def find_z(x, y):
    z0 = 0.0
    # inital root guess; lambda is a compact function to pass z into F
    root = fsolve(lambda z: F(x,y,z), z0)
    return float(root[0])

# Create an empty array in the same shape of X for values of Z
Z = np.empty_like(X, dtype=float)
for i in range(X.shape[0]): #extract x-coordinate
    for j in range(X.shape[1]): #extract y-coordinate
        Z[i, j] = find_z(X[i, j], Y[i, j]) #for each x,y solve z
        
#surface plot of Z(x,y)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title('Z(x,y) in [-0.5,0.5]x[-0.5,0.5]')
plt.show()

#part 2

#function from part 1
f= find_z

#gradient, hessian functions from task 2
def gradient(x, y):
    h = 10**(-3)
    dx = (f(x+h, y)-f(x, y))/h
    dy = (f(x, y+h)-f(x, y))/h
    return (dx, dy)

def hessian(x, y):
    k = 10**(-4)
    dxx = (f(x+k, y)-2*f(x, y)+f(x-k, y))/k**2
    dxy = (f(x+k, y+k)-f(x+k, y)-f(x, y+k)+f(x, y))/k**2
    dyx = (f(x+k, y+k)-f(x+k, y)-f(x, y+k)+f(x, y))/k**2
    dyy = (f(x, y+2*k)-2*f(x, y+k)+f(x, y))/k**2
    return ([dxx, dxy], [dyx, dyy])

#compute gradient, hessian at (0,0)
g= gradient(0,0)
h= hessian (0,0)
print(f'Taylor polynomial P2(x,y)=0+({g[0]:.4f})x+({g[1]:.4f})y+({0.5*h[0][0]:.4f})x**2+({h[0][1]:.4f})xy+({0.5*h[1][1]:.4f})y**2')

#part 3

#Taylor polynomial at (0,0)
def P2(x,y):
    return g[0]*x+g[1]*y+0.5*h[0][0]*x**2+h[0][1]*x*y+h[1][1]*y**2

# Create an empty array in the same shape of X for values of P2
# Iterate through in the same manner as Z
# Calculate values of P2 then plot
P = np.empty_like(X, dtype=float)
for i in range(X.shape[0]): #extract x-coordinates
    for j in range(X.shape[1]): #extract y-coordinates
        P[i, j] = P2(X[i, j], Y[i, j])

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, P)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title('P2(x,y) Taylor approximation')
plt.show()

#part 4

#Absolute error
E = np.abs(Z - P) #plot of absolute error, expect |O(||(x,y)||^3)|

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, E)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title('Absolute error |Z(x,y) - P2(x,y)|')
plt.show()

# The error comes from the Lagrange remainder
# Additionally, we found the taylor coefficients through approximation, which itself will have some amount of error


# git add .
# git commit -m "Your message here"
# git push 