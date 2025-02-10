#arithmetic operators (+,-,/,%,*)
a = 8
b = 5
total = a + b
print("The sum total is:", total)
print(f'The sum total is: {total}')

subtract= a-b
print("The difference is:", subtract)
print(f'The difference is: {subtract}')

multiply = a * b
print("The product is:", multiply)
print(f'The product is: {multiply}')

divide = a / b
print("The quotient is:", divide)
print(f'The quotient is: {divide}')

remainder = a % b
print("The remainder is:", remainder)
print(f'The remainder is: {remainder}')
#comparison operators (==,<,>,<=,>=,!=)
age1 = 21
age2 = 19
comparison1 = age1 == age2
print(f'The output in checking if age 1 is equal to age 2 is: {comparison1}')
comparison2 = age1 < age2
print(f'The output in checking if age 1 is less than age 2 is: {comparison2}')
comparison3 = age1 > age2
print(f'The output in checking if age 1 is greater than age 2 is: {comparison3}')
comparison4 = age1 != age2
print(f'The output in checking if age 1 is not equal to age 2 is: {comparison4}')
comparison5 = age1 >= age2
print(f'The output in checking if age 1 is greater than or equal to age 2 is: {comparison5}')
comparison6 = age1 <= age2
print(f'The output in checking if age 1 is less than or equal to age 2 is: {comparison6}')
#logical operators(and,or,not)
math = 76
english = 56
science = 68
swahili= 58
print(math > english and science > swahili)
print(math < english and science > swahili)
print(math == english and science == swahili)
print(math != english and science != swahili)
print(math != english and science == swahili)
print(math <= english and science >= swahili)
print(math > english or science > swahili)
print(not(math < english or science > swahili))

enter_first_number=float(input("enter first number "))
enter_second_number=float(input("enter second number "))
enter_third_number=float(input("enter third number "))
enter_fourth_number=float(input("enter fourth number "))
divide1 = enter_first_number / enter_second_number
print(f'The output of Quotient1 is:{divide1}')
divide2 = enter_third_number / enter_fourth_number
print(f'The output of Quotient2 is:{divide2}')
comparison1 = divide1 < divide2
print(f'The comparison between quotient1 being less than quotient2 is:{comparison1}')
comparison2 = divide1 > divide2
print(f'The comparison between quotient1 being greater than quotient2 is:{comparison2}')
comparison3 = divide1 >= divide2
print(f'The comparison between quotient1 being greater than/ Equal to quotient2 is:{comparison3}')
comparison4 = divide1 <= divide2
print(f'The comparison between quotient1 being less than/ Equal to quotient2 is:{comparison4}')
comparison5 = divide1 != divide2
print(f'The comparison between quotient1 being not equal to quotient2 is:{comparison5}')
comparison6 = divide1 == divide2
print(f'The comparison between quotient1 being equal to quotient2 is:{comparison6}')
if divide1 > 0:
    print("The number of quotient1 is positive")
elif divide1 < 0:
    print("The number of quotient1 is negative")
else:
    print("The number of quotient1 is zero")

if divide2 > 0:
        print("The number of quotient2 is positive")
elif divide2 < 0:
        print("The number of quotient2 is negative")
else:
        print("The number of quotient2 is zero")
print(divide1 and divide2)
Enter_Username = input("Enter the username: ")
Enter_Password = input("Enter the password: ")
Username = "admin"
password = "secure123"
print(f'Username is: {Enter_Username == Username and Enter_Password == password}')
