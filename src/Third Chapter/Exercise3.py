#Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#
#Write a loop that prints each of the numbers on a new line. (1)
#Write a loop that prints each number and its square on a new line. (2)
#Write a loop that adds all the numbers from the list into a variable called total.
    #You should set the total variable to have the value 0 before you start adding them up, and print the value in total after the loop has completed. (3)
#Print the product of all the numbers in the list. (4)

#1:
#xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#for i in xs:
#    print(i)

#2:
#xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#for i in xs:
#    print(i, i**2)

#3:
#xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#total = 0
#for i in xs:
#   total = total+i
#print(total)

#4:
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
product = 1
for i in xs:
    product = product*i
print(product)
