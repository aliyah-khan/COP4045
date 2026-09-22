#aliyah khan
#2

print("aliyah khan z23556724")
#part a
'''going through every combination of a, b, c, and d from 1 - 10 to see
if a^2 + b^2 equals c^2 + d^2
using four nested for clauses inside the comprehension so every possible
ordering gets checked
len(set) check ensures a, b, c, and d are all different numbers'''
pythagoreanQuadruples = [
    (a, b, c, d)
    for a in range(1, 11)
    for b in range(1, 11)
    for c in range(1, 11)
    for d in range(1, 11)
    if len({a, b, c, d}) == 4 and (a**2 + b**2) == (c**2 + d**2)
]

print("\npart a result: ", pythagoreanQuadruples, sep="")


#part b
'''lowercasing each word, pairing it with its length,
but only keeping the ones shorter than 5 characters'''
words = ['One', 'SEVEN', 'three', 'two', 'Ten']

shortWords = [
    (word.lower(), len(word))
    for word in words
    if len(word) < 5
]

print("\npart b result: ", shortWords, sep="")


#part c
'''splitting each full name into first, middle, and last name, then
#rebuilding it as firstname, middle initial, and lastname'''
names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']

shortNames = [
    name.split()[0] + " " + name.split()[1][0] + ". " + name.split()[2]
    for name in names
]

print("\npart c result: ", shortNames, sep="")


#part d
'''using two for clauses to go through every word from lst1 paired with
every word from lst2
sorting the letters of each word to check if two words are anagrams'''
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

anagramPairs = [
    (w1, w2)
    for w1 in lst1
    for w2 in lst2
    if sorted(w1.lower()) == sorted(w2.lower())
]

print("\npart d result: ", anagramPairs, sep="")


#part e
'''going through each string in s and mapping it to its length'''
s = ['one', 'two', 'three']

wordLengths = {
    word: len(word)
    for word in s
}

print("\npart e result: ", wordLengths, sep="")


#part f
'''going through each index in text and checking if the character at that
index is a vowel
only the vowel index and character pairs get added to the dict'''
text = "Hello world"

vowelPositions = {
    i: text[i]
    for i in range(len(text))
    if text[i].lower() in "aeiou"
}

print("\npart f result: ", vowelPositions, sep="")
