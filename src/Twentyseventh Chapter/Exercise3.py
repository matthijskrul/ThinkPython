# Think of various ways you might save the animal knowledge tree in a file. Implement the one you think is easiest.
class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"


def animal():
    animalfile = open("Animaltree.txt", "w")

    # Start with a singleton
    root = Tree("bird")

    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # Get new information
        prompt  = "What is the animal's name? "
        animal  = input(prompt)
        prompt  = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))
        animalfile.write("Question: ")
        animalfile.write(question)
        animalfile.write("\n")

        # Add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
            animalfile.write("N: ")
            animalfile.write(guess)
            animalfile.write(" "*len(guess))
            animalfile.write("Y: ")
            animalfile.write(animal)
            animalfile.write("\n")
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
            animalfile.write("N: ")
            animalfile.write(animal)
            animalfile.write(" " * len(animal))
            animalfile.write("Y: ")
            animalfile.write(guess)
            animalfile.write("\n")

    animalfile.close()

animal()