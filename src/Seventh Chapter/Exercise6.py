# Count how many words occur in a list up to and including the first occurrence of the word “sam”.
# (Write your unit tests for this case too. What if “sam” does not occur?)


def words_until_sam(list):
    wordcount = 0
    for i in list:
        wordcount += 1
        if i == "sam":
            break
    print(wordcount)


words_until_sam(["isaac", "levi", "daniel", "joshua", "sam", "abraham"])
