#aliyah khan
#1 
import math
import matplotlib.pyplot as plt
import numpy as np

def quadratic(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    #calculating under radical
    radical = (b**2)-(4*a*c)
    if radical < 0:
        print("no real solutions")
    else:
        #calculating entire formula if possible
        plus = ((-b) + (math.sqrt(radical)))/(2*a)
        minus = ((-b) - (math.sqrt(radical)))/(2*a)
        if radical == 0:
            print(f"one solution: {plus:.5f}")
        if radical > 0:
            print(f"two solutions: x1={minus:.5f} x2 ={plus:.5f}")
    return a, b, c, radical

while True:
    a = input("Enter a: ") 
    if a == "":
        break
    b = input("Enter b: ")
    c = input("Enter c: ")
    a, b, c, radical = quadratic(a, b, c)
    print()
    
    if radical < 0:
        #picking domain for no real solutions
        xopt = (-b)/(2*a)
        xmin = xopt - 5
        xmax = xopt + 5
    else:
        #picking domain for one or two solutions
        x1 = ((-b) - math.sqrt(radical))/(2*a)
        x2 = ((-b) + math.sqrt(radical))/(2*a)
        xmin = min(x1, x2) - 2
        xmax = max(x1, x2) + 2
    
    x = np.linspace(xmin, xmax, 150)
    y = a*x**2 + b*x + c
    
    #graphing
    plt.figure()
    plt.plot(x, y)
    plt.axhline(0)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"y = {a}x^2 + {b}x + {c}")
    plt.grid()
    plt.show()
    
    print()








