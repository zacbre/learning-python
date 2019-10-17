print("Hello World!")
print('Hello World 1!')

myint = 7
myfloat = 7.13
mystring = "I'm too lazy"
"""
I'm a multi-line comment!
"""
# I'm a single line comment!

print(myint)
print(myfloat)
print(mystring)

x = 2
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(3 % 2)

z = x + y
print(z)
z = z - y
print(z)

a = "Hello"
b = " "
c = "World"

print(a + b + c)

mystring = None

# When we print these out, these two are not the same.
# None is nothing, and "None" is a string.
print(mystring)
print("None")
                      #  0        1       2        3
myListOfFirstNames = ["James", "John", "Joseph", "Jack"]
myListOfLastNames = ["Johnson", "Smith", "Chui", "Doe"]

print(myListOfFirstNames[0])
print(myListOfLastNames[0])
for i in range(len(myListOfFirstNames)):
    print(myListOfFirstNames[i] + " " + myListOfLastNames[i])

x = 7
if x is 7:
    print("x is equal to 7")
elif x is 8:
    print("x is equal to 8")
else:
    print("x is equal to " + str(x))

