# The rest of the mathematical operators
x = 2 ** 20
print(x)

mysequence = "hello" * 10
print(mysequence)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = list1 + list2
print(list3)

print(list3 * 3)

# String formatting
firstname = "John"
print("Hello, my name is " + firstname + "!")
print("Hello, my name is %s!" % firstname)

age = 20
print("%s is %d years old." % (firstname, age))

# Conditional
y = 10
print(y == 10)
print(y == 9)
print(y < 10)
print(y <= 10)

output = y == 10
print(output)
if output: # y == 10
    print("output is true!")

#in
namelist = ["John", "Bob"]

if firstname in namelist:
    print("The name exists in the array!")

for name in namelist:
    if name == firstname:
        print("The name exists in the array!")

#is
listx = [1, 2, 3]
listy = [1, 2, 3]
print(listx == listy)
print(listx is listy)

number = 1
print(number == 1)
print(number is 1)

#not
print(not False == False)

switch = False

# Same thing
switch = not switch
print(switch)

# Same thing
if switch == True:
    switch = False
elif switch == False:
    switch = True
print(switch)

# Functions
def my_function():
    print("Hello world from my_function!")

my_function()

def hello(name):
    print("Hello my name is %s" % name)


personsname = input("Tell me your name:")
hello(personsname)

class MyClass:
    def print_name(self, name):
        print("Hello, %s, welcome to my class!" % name)

instance = MyClass()
instance.print_name("Edwin")
