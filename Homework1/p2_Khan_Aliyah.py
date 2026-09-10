#2
def find_Pythagorean(n):
    triplesList = []
    triples = ()
    
    #iterating through a, b, and c, each up to n to see if the pythagoream
    #theorem is true for a set of numbers and adding those numbers to the
    #list of tuples
    #using nested for loops ensures cases like (3,4,5) and (4,3,5) are
    #included
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                if ((a**2 + b**2) == (c**2)):
                    triplesList.append((a,b,c))
    print("\nList of pythagorean triples: ", triplesList, sep = "")
     
n = int(input("Enter n: "))
find_Pythagorean(n)
