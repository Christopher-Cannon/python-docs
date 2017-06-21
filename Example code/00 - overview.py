# Printing data
print("Hello world")

# Variables and datatypes
myInt = 12
myFloat = 8.5
myString = "python"
myBoolean = True

myInt += 2

# Mathematics
print(8 + 2 * 3)
print(12 / (3 - 2))
print(8 ** 2)
print(7 // 3)
print(12 % 5)

# Comparison
print(8 < 5)
print(9 > 1)
print(5 == 5)
print(myString == "python")
print(12 != 11)
print(10 <= myInt < 20)
print((myInt >= 10) and (myInt < 20))
print((myFloat == 8.5) or (myFloat == 10.5))
print(not(myBoolean))

# Lists (arrays)
listOne = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listTwo = listOne[1:6]
print(listTwo[2])

listTwo.append(myInt)
listTwo.insert(0, listOne[5])
print(listTwo)

listOne.pop()
del listOne[3]
listTwo.sort()
listTwo.reverse()
print(listTwo)

listThree = listOne + listTwo
print(len(listThree))

listFour = [1] * 9
print(listTwo + listFour)

# If statements
if(myInt > 20):
    print("myInt is larger than 20")
elif(myInt < 10):
    print("myInt is smaller than 10")
else:
    print("myInt is between 10 and 20")

# For loops
for elem in listOne:
    print(elem ** 2)

for x in range(20):
    if(x % 2 == 0):
        print(x)

# While loops
while(myInt > 0):
    print(myInt * myInt)

    myInt -= 1

# Functions
def addTwo(num1, num2):
    return num1 + num2

print(addTwo(5, 10))
print(addTwo(myFloat, listThree[3]))
