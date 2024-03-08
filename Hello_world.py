'''
x = 10
y = 15
z = x + y
for i in range(5):
    print("my number is " + str(z))
'''
# Exercise: if, elif, else statement    
'''
number = -4

if number > 0:
    print("Number is positive.")

elif number == 0:
    print("Number is zero.")
else:
    print("Number is negative.")
 '''
'''
number = 0

if number > 0:
    print("Number is positive.")
elif number == 0:
    print("Number is zero.")
else:
    print("Number is negative.")    
'''


#print(type("2.0"))
#print(type(2.0))
#print(type(2))
#Convert Fahrenheit to Celsius
'''
def to_celsius(x):
    return (x-32) * 5/9


print(to_celsius(100))
'''
#Exercise: Loops and Functions  
'''
def countdown(n):
    while n >= 0:
        print(n)
        n -= 1
        
countdown(5)
'''
#Exercise: Recursion
'''  
def factorial(n):
    if n <= 1:
        return 1
    else:   
        return n * factorial(n - 1)

print(factorial(5))
''' 
#Exercise: Object Oriented Programming 
''' 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 36)
print(person1.name)
print(person1.age)
'''
# Exercise: Classes and Attributes  
'''
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("The Catcher in the Rye", "J.D. Salinger", 287)
print(book1.title)
print(book1.author)
print(book1.pages)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 =  Book("Harry Potter and the Philosopher's Stone", "J.K.", 223) 
print(book1.title)
print(book1.author)
print(book1.pages)

'''
'''
class Student(Person): # Inherit from class Person
    def __init__(self, name, age, grade):
    super().__init__(name, age)
    self.grade = grade

student1 = Student("Charlie Brown", 9, "A")
print(student1.name)
print(student1.age)
print(student1.grade)
'''
#Exercise: veriable type conversion (to string)
'''
base = 6
hight = 3
area =  (base * hight)/2
print("Area of triangle is " +str(area))
'''

#Exercise: Functions
'''
def greeting(name):
    print("Welcome, " + name)
    
greeting("Kay")
greeting("Cameron")
'''
'''
def salam(name):
    print("assalam o alikum, " + name)

salam("ahmad")
salam("ali")
salam("babar")
'''
'''
def intro(name, department):
    print("my name is " + name  + ", and I am in the "+department+" department.")

intro("babar", "commercial")
'''
#Exercise: to determine the type of variables
'''
print(type(40))
'''
#Exercise: veriable conversion (to string)
'''
number = 12
string = str(number)
print(string)
'''
#Exercise: sorted function (number sort)
'''
list =  [9, 11, 2, 5, 8, 9]
print(sorted(list))
'''
#Exercise: sorted function (string sort)
'''
list = "hello"
print(sorted(list))

'''
#Exercise: min and max functions
'''
list = [1,5,3,4,5,6,8,9]
print(min(list))
print (max(list))
'''
#Exercse: input from user
'''
user_input = input("Enter your name : ")
print ("Hello , "+ user_input+". How are you today ?")
'''

'''
user_input = input("Enter your name : ")
print("Hello ", user_input, ". How are you today?" )
'''
#Excerses: while loop
'''
count = 0
while count <= 5:
    print(count)
    count += 1
else:
    print("End of Loop")
'''
#Exerses: for loop with while loop
'''
num = int(input("Enter a number :"))
fact = 1
for i in range(1, num + 1):
   fact *= i
print("The factorial is",fact)
'''
# function definition with return value
'''
def area_triangle(base,hight):
    return base*hight/2

area_1 = area_triangle(4,5)
area_2 = area_triangle(4,6)
sum = area_1  + area_2
print("Sum of the areas of two triangles is", sum)
'''
#function definition without return value
'''
def greating(name):
    print("greating " + name)

result = greating("ahmad")
print(result)
'''
# function definition without return value
'''
def greating(name):
    print("Hi, AssalamAlikum, " + name)

result = greating("Waqar")
print(result)
'''
# function definition with return value
'''
def introduction(name, department):
    return "Hello, " + name + ". Your department is " + department

result = introduction("Muhammad Waqar","Computer Science and Technology")
print(result)
'''

''''
def luckyNumber(name):
    number = len(name) * 9
    print("your name is " + name + ". your lucky number is: " + str(number))
luckyNumber("waqar")
luckyNumber("AhmadAli")
'''
'''
#print(10>1) 
#print(1>2)
#print("cat" != "dog")    #adadsdad

#print( 1 == "1")
#print(15 <= 5*3)
#print(15 <= 5*3)
#print(9/3 == 12/4)

'''
#from selenium  import webdriver

#if statement
'''
def hint_username(username):
    if len(username) <= 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Username is valid.")
hint_username("PJCorum")
'''

#if statement with modolus operator
'''
def is_even(number):
    if number % 2 == 0:
        return True
    return False
print(is_even(6))
print(is_even(7))
'''
# if statement with elif and else
'''
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")
hint_username("PaulJohnson")
hint_username("raza")
hint_username("hafzalraza")
'''
'''
# This function accepts one variable as a parameter
def translate_error_code(error_code):
 
# The if-elif-else block assesses the value of the variable
# passed to the function as a parameter. The if statement uses 
# the equality operator == to test the value of the variable.
# This test returns a Boolean (True/False) result.
    if error_code == "401 Unauthorized":
# If the comparison above returns True, then the indented 
# line(s) inside the if-statement will run. In this case, the
# action is to assign a string to the translation variable.
# The remainder of the if-elif-else block will not run.
# The Python interpreter will skip to the next line outside of 
# the if-elif-else block. In this case, the next line is the 
# return value statement.  
        translation = "Server received an unauthenticated request"
 
# If the initial if-statement returns a False result, then the
# first elif-statement will run a different test on the value
# of the variable.
    elif error_code == "404 Not Found":
# If the first elif-statement returns a True result, then the
# indented line(s) inside the first elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Requested web page not found on server"
 
# If both the initial if-statement and the first elif-statement 
# return a False result, then the second elif-statement will
# run.
    elif error_code == "408 Request Timeout":
# If the second elif-statement returns a True result, then the
# indented line(s) inside the second elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Server request to close unused connection"
 
# If the conditional tests above do not produce a True result
# then the else-statement will run. 
    else:
        translation = "Unknown error code"
# The if-elif-else block ends.

# The next line outside of the if-elif-else block will run
# after exiting the block. In this case, the next line returns
# the output from the if-elif-else block.
    return translation

# The print() function allows us to display the output of the
# function. To call a function in a print statement, the syntax
# is print(name_of_function(parameter))
print(translate_error_code("404 Not Found"))

# Expected output:
# Requested web page not found on server
'''
# Sets value of the "number" variable
'''
number = 25

# The "number" variable will first be compared to 5. Since it is 
# False that "number" is not less than or equal to 5, the expression indented 
# under this line will be ignored. 
if number <= 5: 
   print("The number is 5 or smaller.")
 
# Next, the "number" variable will be compared to 33. Since it is 
# False that "number" is equal to 33, the expression indented under 
# this line will be ignored. 
elif number == 33:
   print("The number is 33.")
 
# Then, the "number" variable will be compared to 32 and 6. Since it 
# is True that 25 is less than 32 and greater than 6, the Python 
# interpreter will print "The number is less than 32 and/or greater
# than 6." Then, it will exit the if-elif-else statement and the remainder 
# of the if-elif-else statement will be ignored.
elif number < 32 and number >= 6:
   print("The number is less than 32 and greater than 6.")
 
else:
   print("The number is " + str(number))
 
# Expected output is: 
# The number is less than 32 and greater than 6.
'''

#excercise if, elif and else statement
'''
number = 5
if number <= 5:
    print("number is less 6")
elif number > 5 and number < 10:
    print("number is between 5 and 10")
else:
    print("number is " + str(number))
'''
# OOPs Concept in python  
'''
class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)
'''
'''
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)   
'''
'''
class Mango:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

chonsa = Mango("yellow", "sweet")
sindri =  Mango("green","tangy")
print("color of chonsa is", chonsa.color)
print("and taste is", chonsa.flavor)
print("color of sindri is",sindri.color)
print("and taste is", sindri.flavor)
   ''' 
# prints "an apple which is red and sweet" 
'''
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)

honeycrisp = Apple("red", "sweet")
figi = Apple("green", "sweet")
print(honeycrisp)
print(figi)
'''
#def __str__(self):
'''
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
jonagold = Apple("red", "sweet")
print(jonagold)
'''
#Classes & Objects
'''
class Dog(object):
    def __init__(self):
        print('Nice you created a dog')
    def speak(self):
        pass
Dog()
Dog()
'''
'''
class Person(object):
    def __init__(self):
        print('you created a person class')

Person()
'''
'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list = [1,2,3]
    def speak(self):
        print('Hi, I am ', self.name, 'my age is', self.age)
    def change_age(self, age):
        self.age = age
        
bark = Dog('bark', 15)
bark.change_age(5)
bark.speak()
print(bark.age)
print(bark.name)
print(bark.list)
'''
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print ("Woof!")


my_dog = Dog('tommy', 7)
print(my_dog.name)
print(my_dog.age)
my_dog.bark()
'''
'''       
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f"You've driven {miles} miles. Your total mileage is now {self.mileage} miles.")

    def fill_gas_tank(self):
        print("Filling the gas tank...")
        self.mileage = 0
        print("Gas tank filled!")

my_car = Car("Toyota", "Camry", 2015)
my_car.drive(100)  # Output: You've driven 100 miles. Your total mileage is now 100 miles.
my_car.fill_gas_tank()  # Output: Filling the gas tank...
                         #         Gas tank filled!
                         '''

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
point1 = Point(10, 100) # create an instance of a point with coordinates (10, 100)
