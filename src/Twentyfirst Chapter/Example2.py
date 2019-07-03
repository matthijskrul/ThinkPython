def multadd (x, y, z):
    return x * y + z

def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))

my_list = [1, 2, 3, 4]
front_and_back(my_list)