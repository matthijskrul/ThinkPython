# Write a program called alice_words.py that creates a text file named alice_words.txt
# containing an alphabetical listing of all the words,
# and the number of times each occurs, in the text version of Alice’s Adventures in Wonderland.

# The first 10 lines of your output file should look something like this:
#
# Word              Count
# =======================
# a                 631
# a-piece           1
# abide             1
# able              1
# about             94
# above             3
# absence           1
# absurd            2

import re


def alice_words(alice):
    wordtally = {}
    alicehandle = open(alice, "r")
    lines = alicehandle.readlines()
    alicehandle.close()
    words = re.findall("[a-zA-Z]+", " ".join(lines))  # easiest way to get rid of \n etc in txt
    for word in words:
        word = word.lower()  # finally a string, so a chance to lowercase it
        wordtally[word] = wordtally.get(word, 0) + 1
    wordlist = list(wordtally.items())
    wordlist.sort()
    alicefile = open("alice_words.txt", "w")
    alicefile.write("\n")
    alicefile.write("Word")
    alicefile.write("              ")
    alicefile.write("Count\n")
    alicefile.write("=======================\n")
    for i in wordlist:
        alicefile.write(i[0])
        alicefile.write(str(i[1]).rjust((23-len(i[0]))))  # 23 characters until end of 'Count', so right align to there
        alicefile.write("\n")
    alicefile.close()


alice_words("C:\\Users\Matthijs\Programming\ThinkPython\src\Twentieth Chapter\\alice_in_wonderland.txt")


#  NB: English syntax poses a problem here: omitting ' in the RE Findall method means "Alice's" is treated as
#  one instance of the word "Alice" and one instance of the word "s". It also leads to pseudowords like "doesn".
#  Conversely, including the ' leads to the appearance of many words that open a sequence in quote marks in the text,
#  e.g. " 'besides ". The latter seems more distorting than the former, so I have omitted the (possessive) apostrophe.
