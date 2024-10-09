import math

def f(x):
    y = (1) / (x**2 + 1) + (x**2)
    return y 

def parametrcycle(a, b, h):
    resultlist = list()

    for i in range(int(a), int(b),int(h)):
        resultlist.append(f(i))

    return resultlist

def conditionalcycle(a, b, h):
    resultlist = list()

    i = int(a)
    while i < int(b):
        resultlist.append(f(i))
        i += int(h)

        return resultlist 

a = input("a: ")
b = input("b: ")
h = input("h: ")

print("\n")

print("parametercycle values:")
for y in parametrcycle(a, b, h):
    print(y)

print("\n")

print("conditionalcycle values:")
for y in conditionalcycle(a, b, h):
    print(y)

print("\n")

print("sorted parametrcycle values:")
sortedlist = sorted(parametrcycle(a, b, h))
for y in sortedlist:
    print(y)

    print("\n")

print("sorted conditinalcycle values:")
sortedlist = sorted(conditionalcycle(a, b, h))
for y in sortedlist:
    print(y)

