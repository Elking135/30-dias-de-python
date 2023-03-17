1.1
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

1.2
number2 = [10,9,8,7,6,5,4,3,2,1, 0]
for number in number2:
    print(number)

1.3
h = "#"

for yea in range(1,9):
    yea = yea * h
    print(yea)

1.4
hags_2 = "#"

for i in range(1,9):
    for r in range(1,9):
        print(hags_2, end="")

1.5
for sus in range(0,11):
    print(sus, "x", sus, "=", sus*sus)

1.6
pep = ["Python", "Numpy", "Pandas", "Diango", "Flask"]

for contents in pep:
    print(contents)

1.7
for i in range(0,51):
    print(2 * i)


1.8
for i in range(0,50):
    print(2 * i + 1)


2.1
total = 0

for i in range(101):
    total += i

print("The sum of all numbers from 0 to 100 is: ", total)
