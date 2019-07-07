class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score  # Less is more