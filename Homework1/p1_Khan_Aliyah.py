import math
import matplotlib.pyplot as plt
import numpy as np

#q1
def quadratic(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    radical = (b**2)-(4*a*c)
    if radical < 0:
        print("no real solutions")
    else:
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
    
    #choose the graph domain
    if radical < 0:
        xopt = -b/(2*a)
        xmin = xopt - 5
        xmax = xopt + 5
    else:
        x1 = ((-b) - math.sqrt(radical))/(2*a)
        x2 = ((-b) + math.sqrt(radical))/(2*a)
        xmin = min(x1, x2) - 2
        xmax = max(x1, x2) + 2
    
    #make 150 x values
    x = np.linspace(xmin, xmax, 150)
    
    #calculate y values
    y = a*x**2 + b*x + c
    
    #make the graph
    plt.figure()
    plt.plot(x, y)
    plt.axhline(0)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"y = {a}x^2 + {b}x + {c}")
    plt.grid()
    plt.show()
    
    print()








