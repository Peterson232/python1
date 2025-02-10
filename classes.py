class Student:
    first_name = "James"
    last_name = "Gichuru"
    gender = "male"
    age = 23
class Person:
    def __init__(self, name, gender, marital_status,occupation):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation

    def salute(self):
        print(f'Good Morning, {self.name}! You are {self.marital_status}')

    def display_name(self):
        print(f'You are {self.name} of gender {self.gender}')
class Vehicle:
    def __init__(self, brand, model, year):
        self.make = brand
        self.model = model
        self.year = year

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
    def calculate_area(self):
        return (self.width * self.length)
