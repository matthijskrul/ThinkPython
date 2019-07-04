# 1) Write a Boolean function between that takes two MyTime objects, t1 and t2, as arguments,
# and returns True if the invoking object falls between the two times.
# Assume t1 <= t2, and make the test closed at the lower bound and open at the upper bound,
# i.e. return True if t1 <= obj < t2.
# 2) Turn the above function into a method in the MyTime class.
# 3) Overload the necessary operator(s) so that instead of having to write
#
# if t1.after(t2): ...
# we can use the more convenient
#
# if t1 > t2: ...
# 4) Rewrite increment as a method that uses our “Aha” insight.
# 5) Create some test cases for the increment method.
# Consider specifically the case where the number of seconds to add to the time is negative.
# Fix up increment so that it handles this case if it does not do so already.
# (You may assume that you will never subtract more seconds than are in the time object.)


class MyTime:  # imported from example

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600  # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def increment_rewrite(self, seconds):   # increment rewrite
        self.seconds = self.to_seconds() + seconds
        self.hours = self.seconds // 3600
        self.minutes = (self.seconds % 3600) // 60
        self.seconds = self.seconds % 3600 % 60
        return self.hours, self.minutes, self.seconds

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __gt__(self, other):  # overload of operator
        return self.after(other)

    def between(self, t1, t2):  # new function as method
        t1 = t1.to_seconds()
        t2 = t2.to_seconds()
        if t1 <= self.to_seconds() < t2:
            return True
        return False


t = MyTime(0, 0, 480)
print(t.increment_rewrite(-120))