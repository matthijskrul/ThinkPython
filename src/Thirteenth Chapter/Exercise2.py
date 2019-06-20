# Write a program that reads a file and prints only those lines that contain the substring 'snake'.


def write_snakeline(f):
    file = open(f)
    lines = file.readlines()
    file.close()
    newtext = []
    substring = "snake"
    for line in lines:
        if substring.lower() in line.lower():
            newtext.append(line)
    newfile = open("snakefile.txt", "w")
    for n in newtext:
        newfile.write(n)
    newfile.close()


write_snakeline(r"C:\Users\Matthijs\Programming\ThinkPython\src\Thirteenth Chapter\Snaketest")
