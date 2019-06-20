# Write a program that reads a text file and produces an output file which is a copy of the file,
# except the first five columns of each line contain a four digit line number, followed by a space.
# Start numbering the first line in the output file at 1.
# Ensure that every line number is formatted to the same width in the output file.
# Use one of your Python programs as test data for this exercise:
# your output should be a printed and numbered listing of the Python program.


def numbered_file(f):
    file = open(f)
    lines = file.readlines()
    file.close()
    count = 1
    newtext = []
    for line in lines:
        newtext.append("%04d" % count)
        newtext.append(" ")
        newtext.append(line)
        count += 1
    newfile = open("numberedfile.txt", "w")
    for n in newtext:
        newfile.write(n)
    newfile.close()


numbered_file(r"C:\Users\Matthijs\Programming\ThinkPython\src\Thirteenth Chapter\Exercise1.py")