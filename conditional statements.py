# if....else..
# while loop
votes = 5001
if votes > 5000:
    print(f"you got {votes} and therefore you are the winner")
else:
    print(f"you got {votes} and therefore you did not win")
enter_number = float(input("enter a number: "))
if enter_number > 0:
    print(f"The number entered is a positive number")
elif enter_number < 0:
    print(f"The number entered is a negative number")
else:
    print(f"The number entered is zero ")

#exam grading system
mark = 82
if mark > 80 and mark <= 100:
    print(f"you got {mark} and therefore you get grade A!")
elif mark > 70 and mark <= 80:
    print(f"you got {mark} and therefore you get grade B!")
elif mark > 60 and mark <= 70:
    print(f"you got {mark} and therefore you get grade C!")
elif mark > 50 and mark <= 60:
    print(f"you got {mark} and therefore you get grade D!")
elif mark > 30 and mark <= 50:
    print(f"you got {mark} and therefore you get grade E!")
elif mark <=30 and mark >=0:
    print(f"you got {mark} and therefore you fail")
else:
    print(f"please enter a number betweeen 0 and 100")

enter_age = float(input(f"enter your age in years: "))
if enter_age <= 2:
    print(f"you are a baby")
elif enter_age > 2 and enter_age <= 3:
    print(f"you are a toddler")
elif enter_age >= 4 and enter_age <= 12:
    print(f"you are a child")
elif enter_age >= 13 and enter_age <= 19:
    print(f"you are a teenager")
elif enter_age >= 20 and enter_age <= 34:
    print(f"you are a young adult")
elif enter_age >= 35 and enter_age <= 59:
    print(f"you are a middle aged adult")
elif enter_age >= 60 :
    print(f"you are a senior citizen")
print(f"Age is just a number, enjoy life")


current_temperature = float(input("enter your current temperature in celcius: "))
if current_temperature > 30:
    print(f"It's a hot day")
elif current_temperature >20 and current_temperature <=30:
    print(f"It's a warm day")
elif current_temperature <=20:
    print(f"It's a cold day")
else:
    print(f"enter an appropiate temperature")
