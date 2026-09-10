#3
def find_dup_str(s, n):
    #checking every possible first substring
    for i in range(len(s) - n + 1):
        sub = s[i:i+n]
        #starting after the first substring to avoid overlap
        for j in range(i + n, len(s) - n + 1):
            if sub == s[j:j+n]:
                return sub
    return ""


def find_max_dup(s):
    #starting with the longest possible substring and going down
    for n in range(len(s), 0, -1):
        #calling function above to see if a duplicate of the
        #same length exists
        result = find_dup_str(s, n)
        if result != "":
            return result
    return ""

s = input("Enter a string: ")
n = int(input("Enter substring length: "))

print("\nDuplicated substring of length ", n, ": ", find_dup_str(s, n), sep = "")
print("Longest duplicated substring:", find_max_dup(s))
