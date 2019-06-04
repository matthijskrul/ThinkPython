p = 10000
n = 12
r = 0.08
t = int(input("For how many years should the interest be compounded? "))
amount = (p*(1+r/n)**(n*t))
print(amount)