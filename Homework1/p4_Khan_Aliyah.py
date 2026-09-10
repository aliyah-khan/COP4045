#aliyah khan
#4
import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    xmin, xmax = domain
    
    #creating a list of x values by calculating
    #average distance between each point
    xlist = []
    split = (xmax - xmin) / (ns - 1)
    for i in range(ns):
        x = xmin + i * split
        xlist.append(x)
    
    #calculating y values by inputting x
    #into the user's formula
    ylist = []
    for x in xlist:
        y = eval(fun_str)
        ylist.append(y)
        
    #printing the table of points
    print("\n       x          y")
    print("-----------------------")
    
    for i in range(min(12, len(xlist))):
        print(f"{xlist[i]:10.4f} {ylist[i]:10.4f}")
    if len(xlist) > 12:
        print("----------------------- (rest of the table not shown)")
    else:
        print("-----------------------")
    
    #making graph
    plt.plot(xlist, ylist, "o-")
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
