import random
import matplotlib.pyplot as plt

mylist = []

for i in range(0,100):
    x = random.randint(0,9)
    mylist.append(x)

print("The random list generated is: ", mylist)

print("\n")
zero = mylist.count(0)
print("The number of times 0 is repeated", zero)

one = mylist.count(1)
print("The number of times 1 is repeated", one)

two = mylist.count(2)
print("The number of times 2 is repeated", two)

three = mylist.count(3)
print("The number of times 3 is repeated", three)

four = mylist.count(4)
print("The number of times 4 is repeated", four)

five = mylist.count(5)
print("The number of times 5 is repeated", five)

six = mylist.count(6)
print("The number of times 6 is repeated", six)

seven = mylist.count(7)
print("The number of times 7 is repeated", seven)

eight = mylist.count(8)
print("The number of times 8 is repeated", eight)

nine = mylist.count(9)
print("The number of times 9 is repeated", nine)

xaxis = [1,2,3,4,5,6,7,8,9]
yaxis = [one, two, three, four, five, six, seven, eight, nine]
print(yaxis)

plt.plot(xaxis, yaxis)
plt.title("Digits vs Frequency")
plt.xlabel("Digits")
plt.xticks(range (1,10,1))
plt.yticks(range (1,15,1))
plt.ylabel("Frequency")
plt.show()