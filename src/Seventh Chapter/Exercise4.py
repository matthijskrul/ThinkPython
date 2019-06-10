# Count how many words in a list have length 5.


def five_long(list):
    fivecount = 0
    for i in (list):
        if len(i) == 5:
            fivecount += 1
    print(fivecount)


five_long(["Broom", "Jingle", "Waterspout", "Medic", "Water", "Abraham"])
