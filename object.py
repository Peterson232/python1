from classes import Student, Person, Vehicle, Rectangle

student1 = Student()
print(student1.first_name)
print(student1.last_name)
print(student1.gender)
print(student1.age)

person1 = Person("Matthew","male","Single","Doctor")
person2 = Person("Irene","female","Single","Lawyer")
person3 = Person("Ben","male","married","Teacher")
print(person1.marital_status)
print(person2.gender)
print(person3.name)
person1.salute()
person2.salute()
person3.salute()
person1.display_name()
person2.display_name()
person3.display_name()

vehicle1 = Vehicle("Audi","Q7","2024")
vehicle2 = Vehicle("Mercedes","C63","2023")
vehicle3 = Vehicle("BMW","M4","2024")
vehicle4 = Vehicle("Toyota","Supra","2022")
print(vehicle1.model)
print(vehicle2.model)
print(vehicle3.model)
print(vehicle4.model)

Perimeter = Rectangle(70,50)
perimeter = Perimeter.calculate_perimeter()
print(f'Perimeter of the rectangle is {perimeter}')
Area= Rectangle(10,10)
area = Area.calculate_area()
print(f'Area of the rectangle is {area}')
Measurement = Rectangle(10, 10)
print(f'The width entered is: {Measurement.width}')
print(f'The length entered is: {Measurement.length}')



