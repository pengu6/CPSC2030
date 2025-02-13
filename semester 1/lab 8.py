def is_blank(line):
    """Return True if a line is blank

    Blank lines may include whitespace, but not other characters

    :param line: String representing a line of text
    :return: Boolean that will be True if the line contains only whitespace
    """
    if line.isspace() == True:
        return True
    elif line == "":
        return True
    else:
        return False



assert is_blank("") == True
assert is_blank("\n") == True
assert is_blank("a\n") == False
assert is_blank(" \n") == True
assert is_blank("    \n") == True
assert is_blank("  b  \n") == False


def is_comment(line):
    """Return True if a line is a comment

    Comments start with `#`, but whitespace may precede that character

    :param line: String representing a line of text
    :return: Boolean that will be True if line is a comment
    """
    if "#" in line:
        if line.startswith("#") == True:
            return True
        else:
            for char in line:
                if char.isalnum() == True:
                    return False
                elif char.isspace() == True:
                    pass
                elif char == "#": 
                    return True
    else:
        return False


assert is_comment("") == False
assert is_comment("\n") == False
assert is_comment(" \n") == False
assert is_comment("#\n") == True
assert is_comment("    # a\n") == True
assert is_comment("  # comment\n") == True
assert is_comment("print('#')\n") == False


# Your program begins here
# Remeber to use the functions that you tested above to help avoid errors

openfile = input("Enter Python file you'd like to open: ")
writefile = input("Enter a file you'd like to write to: ")

readthisfile = open(openfile)
lines = readthisfile.readlines()

linecount = 0
blanklinecount = 0
commentcount = 0
sloccount = 0

for line in lines: 
    linecount += 1
    if is_blank(line) == True:
        blanklinecount += 1 
    elif is_comment(line) == True:
        commentcount += 1
    else:
        sloccount += 1


with open(writefile, "w") as writethis:
    writethis.write(f"File name {openfile} \n")
    writethis.write(f"Line {linecount} \n")
    writethis.write(f"Blank lines {blanklinecount} \n")
    writethis.write(f"Comments {commentcount} \n")
    writethis.write(f"SLOC {sloccount} \n")
                        

