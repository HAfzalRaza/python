#function that add two numbers
'''
def add_two_numbers(x,y):
    total = x+y
    return total
output = add_two_numbers(3,4)
print(output)
'''
# List
'''
fruits=['apple','banana','cherry']
fruits.append("guava")

print(fruits)
name = fruits.pop()
print(name)
print (fruits)
fruits.append('angur')
print(fruits)
fruits.pop()
print(fruits)

fruits.remove('apple')
print(fruits)
fruits.append('guava')
print(fruits)
fruits.remove('cherry')
print(fruits)
fruits.append('cherry')
print(fruits)

fruits.append(9)
print(fruits)
print(type(fruits))
'''

#tuples

'''
names =('john', 'jane', 'jackson')
print(names)
print(type(names))
names = (1,2,3,'jane')
print(names)
'''
# if elif and eslse condictions
'''
x = 65
if x > 70:
    print('high score')
elif x > 60:
    print('good job')
else:
    print('you did it!')
'''
# For loop
'''
def print_sq_value(numbers):
    for num in numbers:
        sq = num*num
        print('the sq root of ', num , 'is' , sq)
numbers = [1,2,3,4,5]
print_sq_value(numbers)
'''
#while loop & Input() function
'''
user_input = input('what is to be done ? ')

print(user_input)
'''

user_input = 'random value'

def show_menu():
    print('menu')
    print('1. Add an item: ')
    print('2. Mark as done: ')
    print('3. View item: ')
    print('4. Exit ')
while user_input != '4':
    show_menu()
    user_input = input('enter your choice: ')
    if user_input == '1':
        print('add an item')
    elif user_input == '2':
        print('marked as done')
    elif user_input == '3':
        print('view items')
    elif user_input ==  '4':
        print('Goodbye')
    else:
        print("Choose one from the 1, 2, 3, 4")
    


    print(user_input)

print('Goodbye!')
