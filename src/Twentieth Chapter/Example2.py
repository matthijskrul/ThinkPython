opposites = {"up": "down", "right": "wrong", "yes": "no"}
alias = opposites
copy = opposites.copy()

alias["right"] = "left"
#opposites["right"] # when called (say in console) returns 'left'

copy["right"] = "privilege"
#opposites["right"] # when called still returns 'left'