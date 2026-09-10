def find_dup_str(s, n):
    #check every possible first substring
    for i in range(len(s) - n + 1):
        sub = s[i:i+n]
        
        #start after the first substring to avoid overlap
        for j in range(i + n, len(s) - n + 1):
            if sub == s[j:j+n]:
                return sub
    return ""


def find_max_dup(s):
    #start with the longest possible substring
    for n in range(len(s), 0, -1):
        result = find_dup_str(s, n)
        if result != "":
            return result
    return ""

s = input("Enter a string: ")
n = int(input("Enter substring length: "))

print(find_dup_str(s, n))
print(find_max_dup(s))
