# Write a program that reads a file and writes out a new file with the lines in reversed order
# (i.e. the first line in the old file becomes the last one in the new file.)


def reverse_file(f):
    newlines = []
    file = open(f)
    lines = file.readlines()
    file.close()
    count = 1
    for line in range(len(lines)):
        newline = lines[-count]
        newlines.append(newline)
        if count == 1:
            newlines.append("\n")
        count += 1
    newfile = open("newf.txt", "w")
    for n in newlines:
        newfile.write(n)
    newfile.close()


# alternatively:


def reverse_file2(f):
    file = open(f)
    lines = file.readlines()
    file.close()
    lines.reverse()
    newfile = open("newfile.txt", "w")
    for n in lines:
        newfile.write(n)
        if n == lines[0]:
            newfile.write("\n")
    newfile.close()

