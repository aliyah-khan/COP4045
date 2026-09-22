#aliyah khan
#1

def line_number(infile: str, outfile: str) -> None:
    """reads infile and writes each line to outfile with the line number in front"""
    try:
        f = open(infile, "r")
        lines = f.readlines()
        f.close()

        out = open(outfile, "w")
        count = 1
        for line in lines:
            out.write(str(count) + ". " + line)
            if not line.endswith("\n"):
                out.write("\n")
            count = count + 1
        out.close()

    except Exception as e:
        print("something went wrong reading or writing the file:", e)
        raise


def findcommentindex(line):
    #finds where a comment starts, ignoring a # if it's inside quotes
    insidequote = False
    quotechar = ""
    index = 0
    while index < len(line):
        ch = line[index]
        if insidequote:
            if ch == quotechar:
                insidequote = False
        else:
            if ch == '"' or ch == "'":
                insidequote = True
                quotechar = ch
            elif ch == "#":
                return index
        index = index + 1
    return -1


def parse_functions(filename: str) -> tuple:
    """parses filename and returns a tuple of tuples, one per top level function,
    sorted by name, as (line number, function name, argument list, function code)"""
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()

        funcs = []
        i = 0
        while i < len(lines):
            line = lines[i]

            if line.startswith("def "):
                startline = i + 1

                #pulling out the function name and argument list
                openparen = line.find("(")
                closeparen = line.find(")")
                name = line[4:openparen].strip()
                args = line[openparen + 1:closeparen].strip()

                #collecting the lines that belong to this function
                codelines = []
                j = i
                while j < len(lines):
                    current = lines[j]

                    #stopping once we reach another line with no indent
                    if j > i:
                        indent = len(current) - len(current.lstrip())
                        if current.strip() != "" and indent == 0:
                            break

                    #cutting off a comment if the line has one
                    commentindex = findcommentindex(current)
                    if commentindex != -1:
                        current = current[:commentindex]
                    current = current.rstrip()

                    if current.strip() != "":
                        codelines.append(current)

                    j = j + 1

                code = ""
                for codeline in codelines:
                    code = code + codeline + "\n"

                funcs.append((startline, name, args, code))
                i = j

            else:
                i = i + 1

        #sorting the functions alphabetically by name with a selection sort
        n = len(funcs)
        for x in range(n):
            smallest = x
            for y in range(x + 1, n):
                if funcs[y][1] < funcs[smallest][1]:
                    smallest = y
            if smallest != x:
                temp = funcs[x]
                funcs[x] = funcs[smallest]
                funcs[smallest] = temp

        return tuple(funcs)

    except Exception as e:
        print("something went wrong parsing the file:", e)
        raise


def main():
    print("aliyah khan z23556724")
    thisfile = "p1_Khan_Aliyah.py"

    #testing line_number, writing to a new file so i don't overwrite this one
    outfile = thisfile + ".txt"
    line_number(thisfile, outfile)
    print("wrote numbered lines of", thisfile, "to", outfile)

    #testing parse_functions
    funcs = parse_functions(thisfile)
    print()
    print("parse_functions result:")
    for func in funcs:
        linenum = func[0]
        name = func[1]
        args = func[2]
        code = func[3]
        print()
        print("line", linenum, ":", name, "(", args, ")")
        print(code)


if __name__ == "__main__":
    main()
