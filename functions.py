def my_function():
    print("Hello World")
    print("Hello world")
my_function()
my_function()
my_function()

def my_string():
    salutation = "Hello World"
    print(salutation)

my_string()

def my_arg(salutation):
    print(salutation)

my_arg("Hello world")
my_arg("Hello Peter")
my_arg("Hello Smith")

def employee(name,gender,age):
    print(f'Hello {name}, your gender is {gender} and you are {age} years old')
employee('Harrison','male',22)
employee('Smith', 'male',19)

def number(number1, number2):
    Sum=number1+number2
    return Sum
print(number(50,50))

def age_calc(current_age):
    new_age=current_age+10
    return new_age
print(age_calc(20))

def promote(name,age):
    if age >= 5 and age <= 7:
        return f'{name} is {age} years old and is promoted to grade 1'
    elif age == 8:
        return f'{name} is {age} years old and is promoted to grade 2'
    elif age <= 10:
        return f'{name} is {age} years old and is promoted to grade 3'
    else:
        return f'{name} is {age} years old and not supposed to be here'

print(promote('Angela',7))
print(promote('Paul',8))
print(promote('James',9))

def greet(name):
    if name == 'Alice' or name == 'Bob':
        return f'Hello {name}, how is your day?'
    else:
        return f'Hi there, how are you?'
print(greet('Alice'))
print(greet('Bob'))
print(greet('James'))
print(greet('Smith'))
