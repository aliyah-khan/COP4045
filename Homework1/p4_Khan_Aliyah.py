import math
import matplotlib.pyplot as plt

#q4
def plot_function(fun_str, domain, ns):
    xmin, xmax = domain
    
    #creating a list of x values by calculating
    #average distance between each point
    xs = []
    split = (xmax - xmin) / (ns - 1)
    for i in range(ns):
        x = xmin + i * split
        xs.append(x)
    
    #calculating y values by inputting x
    #into the given formula
    ys = []
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
        
    #printing the table of points
    print("       x       y")
    print("-----------------------")
    
    for i in range(min(12, len(xs))):
        print(f"{xs[i]:10.4f} {ys[i]:10.4f}")
    if len(xs) > 12:
        print("----------------------- (rest of the table not shown)")
    else:
        print("-----------------------")
    
    #making graph
    plt.plot(xs, ys, "o-")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    plt.grid()
    plt.show()


fun_str = input("Enter function with variable x: ")
ns = int(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
domain = (xmin, xmax)
plot_function(fun_str, domain, ns)
