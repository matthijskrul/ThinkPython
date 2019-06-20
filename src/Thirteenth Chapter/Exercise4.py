# Write a program that undoes the numbering of the previous exercise:
# it should read a file with numbered lines and produce another file without line numbers.


def denumbered_file(f):
    file = open(f)
    lines = file.readlines()
    file.close()
    newtext = []
    for line in lines:
        newtext.append(line[5:])
    newfile = open("denumberedfile.txt", "w")
    for n in newtext:
        newfile.write(n)
    newfile.close()


denumbered_file(r"C:\Users\Matthijs\Programming\ThinkPython\src\Thirteenth Chapter\numberedfile.txt")
