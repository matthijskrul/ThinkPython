# You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3 (a Wed).
# You return home after 137 sleeps.
# Write a general version of the program which asks for the starting day number, and the length of your stay,
# and it will tell you the name of day of the week you will return on.

weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def day_count():
    start_day = int(input("What is the starting day number? "))
    stay_length = int(input("And for how long are you staying? "))
    return_day = (start_day + stay_length) % 7
    print(weekday[return_day])


day_count()
