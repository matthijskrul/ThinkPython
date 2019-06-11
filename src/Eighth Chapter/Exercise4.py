# Print a neat looking multiplication table (as shown in textbook)

layout = "{0:>4}{1}{2:>6}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>5}{11:>5}{12:>5}{13:>5}"

print(layout.format("", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
print(layout.format("", ":", "------", "----", "----", "----", "----", "----", "----", "----", "-----", "-----", "-----", "-----"))
for i in range(1, 13):
    print(layout.format(i, ":", i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))
