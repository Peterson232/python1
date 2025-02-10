print("hello world")
print("hello world")
print("hello world")
print(2452)
print(23.54)

#variables
age=23
print(age)

first_name="John"
print(first_name)

weight=54.2
print(weight)

#data types
#integer
a= 23423
print(a)
#string
b="please fill this form"
c= "35325"
#boolean
is_boy=True
is_girl=False
#float
x=21.3
print(x)

#input from user
last_name = input("what is your last name? ")
print(last_name)
age = input("how old are you? ")
print(age)
weight = input("how much do you weigh? ")
print(weight)
input_first_number= input(" enter first number ")
input_second_number= input(" enter second number ")
sum= float(input_first_number) + float(input_second_number)
print(sum)
input_weight= float(input(" enter weight in kg "))
input_height = float(input(" enter height im meters "))
bmi = calculate_bmi(input_weight, input_height)
print(f"Your BMI is {bmi: .2f}")
#classify bmi
if bmi < 18.5:
    print("You are under weight.")
elif 18.5 <= bmi < 24.9:
    print("You are normal weight")
elif 25 <= bmi < 29.9:
    print("You are over weight")
else:
    print("You are obese.")