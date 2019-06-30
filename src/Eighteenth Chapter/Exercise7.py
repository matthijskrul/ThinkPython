# Write a program that walks a directory structure (as in the last section of this chapter),
# but instead of printing filenames,
# it returns a list of all the full paths of files in the directory or the subdirectories.
# (Don’t include directories in this list — just files.)

import os


def get_dirlist(path):
    outputlist = []
    dirlist = os.listdir(path)
    dirlist.sort()
    for f in dirlist:
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            if get_dirlist(fullname) is None:
                continue
            else:
                outputlist.extend((get_dirlist(fullname)))
        outputlist.append(fullname)
    print(outputlist)


get_dirlist("C:\\Users\Matthijs\Programming\ThinkPython\src")
