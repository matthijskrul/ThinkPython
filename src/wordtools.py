# Create a module named wordtools.py with our test scaffolding in place.
#
# Now add functions so these tests pass:

from unit_tester import test
import string


def cleanword(s):
    newstring = []
    for i in range(len(s)):
        if s[i] not in string.punctuation:
            newstring.append(s[i])
    return "".join(newstring)


def has_dashdash(s):
    if "--" in s:
        return True
    else:
        return False


def extract_words(s):
    lowerlist = s.lower()
    for char in lowerlist:
       if not char.isalnum():
           lowerlist = lowerlist.replace(char, ' ')
    return lowerlist.split()


def wordcount(w, l):
    count = 0
    for i in l:
        if i == w:
            count += 1
    return count


def wordset(l):
    wordlist = []
    for word in l:
        if word in wordlist:
            continue
        else:
            wordlist.append(word)
    return sorted(wordlist)


def longestword(l):
    charlist = []
    if charlist != l:  # very hacky!
        for word in l:
            charlist.append(len(word))
        return max(charlist)
    else:
        return 0


test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
test(longestword(["%", "2", "55"]) == 2)  # added test myself
