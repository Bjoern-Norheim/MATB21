import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import math


# asking user for the function
func = input("Type in a function of x and y: ")

# defining function that will be put in by the user
def f(x, y):
    return eval(func, {"x": x, "y": y, "math": math})

# asking user for the values
x = float(input("x: "))
y = float(input("y: "))

# defining gradient
def gradient(x, y):
    h = 10**(-8)
    dx = (f(x+h, y)-f(x, y))/h
    dy = (f(x, y+h)-f(x, y))/h
    return (dx, dy)

# defining hessian
def hessian(x, y):
    h = 10**(-8)
    k = 10**(-4)
    # dxx = (f(x+2*h,y)-2*f(x+h,y)+f(x,y))/h**2
    dxx = (f(x+k, y)-2*f(x, y)+f(x-k, y))/k**2
    dxy = (f(x+k, y+k)-f(x+k, y)-f(x, y+k)+f(x, y))/k**2
    dyx = (f(x+k, y+k)-f(x+k, y)-f(x, y+k)+f(x, y))/k**2
    dyy = (f(x, y+2*k)-2*f(x, y+k)+f(x, y))/k**2
    return ([dxx, dxy], [dyx, dyy])

# Gradient call for custom function
print("Gradient is: "+str(gradient(x, y)))
# Hessian call for custom function
print("Hessian is: "+str(hessian(x,y)))

# Define function as sin(x+y)
func = "math.sin(x+y)"


# Sin gradient test
sinTest = input("Test gradient function for Sin(x+y)? y/n ")
if sinTest == "y":
    testx = math.pi/4
    testy = math.pi/4
    # Analytical Gradient to compare
    realVal = (math.cos(math.pi/2), math.cos(math.pi/2))
    testGrad = gradient(testx,testy)
    print(gradient(testx,testy))
    print("Error = (" + str(realVal[0]-testGrad[0]) + ", "+ str(realVal[1]-testGrad[1]) +")")

# Sin hessian test
sinTestH = input("Test Hessian function for Sin(x+y)? y/n ")
if sinTestH == "y":
    testx = math.pi/4
    testy = math.pi/4
    # Analytical Hessian to compare
    realVal = ([-1*math.sin(math.pi/2), -1*math.sin(math.pi/2)], [-1*math.sin(math.pi/2), -1*math.sin(math.pi/2)])
    testHess = hessian(testx,testy)
    print(hessian(testx,testy))
    print("Error = ["+ str(realVal[0][0]-testHess[0][0])+", "+ str(realVal[0][1]-testHess[0][1])+"]\n[" 
    + str(realVal[1][0]-testHess[1][0])+", "+ str(realVal[1][1]-testHess[1][1])+"]")





'''QUESTIONS
Test your approximation of the gradient on the function sin(x + y) and compare to the analytical gradient: tested on (0,0), it was exactly the same value as analytical gradient - (1.0,1.0)
Compute the error of your approximation in the point (x, y) = (π/4, π/4). What happens with the error when you change h?: with the original h I got the same exact result (0.0,0.0), once I put h as bigger value (10e-3) I got approximately (-0.0005, -0.0005), so further from the actual value
'''


# New test function
# Function must be a string for eval to compute it as code
func = "8*x*y - 4*y*x**2 - 2*x*y**2 + (x**2)*y**2"


x = float(1)
y = float(2)

print("Gradient at maxima from problem 1 is "+str(gradient(x,y))+" and hessian is " + str(hessian(x,y)))


'''QUESTIONS
Test your approximation of the Hessian on the function sin(x+y) and compare it to the analytical Hessian: it is very close for k being 10e-4
Pick one of the functions from Equation (2) and compute the gradient and Hessian at the local extrema you found in Task 1. Are the results as you would expect?: We picked function f with extrema at (1,2), here the gradient was approx. (-0.004, -0.001) so basically (0,0) as it should be and then the Hessian produces negative output making it local maxima which is true.

'''