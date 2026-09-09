import math
import matplotlib.pyplot as plt
import numpy as np

#notes: make the for loop into a while
#loop that exits as specified on assignment
#also plot the fucking graph UGH
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

while True:
    a = input("Enter a: ")
    if a == "":
        break
    b = input("Enter b: ")
    c = input("Enter c: ")
    quadratic(a, b, c)
    print()
print()

#2
def find_Pythagorean(n):
    triplesList = []
    triples = ()
    
    #iterating through a, b, and c to see if the pythagoream theorem
    #is true for a set of numbers and adding those numbers to the
    #list of tuples
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                if ((a**2 + b**2) == (c**2)):
                    triplesList.append((a,b,c))
    print("\nList of pythagorean triples: ", triplesList, sep = "")
     
n = int(input("Enter n: "))
find_Pythagorean(n)

#3





