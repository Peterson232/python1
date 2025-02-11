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
class My_Employee():
    def __init__(self, name, basic_salary, gender, age):
        self.name = name
        self.basic_salary = basic_salary
        self.gender = gender
        self.age = age

    def my_salary(self):
        my_salary = (self.basic_salary + 41500)
        return my_salary
class Developer(My_Employee):
    def __init__(self, name, basic_salary, gender, age,prog_language):
        super().__init__(name,basic_salary,gender,age)
        self.prog_language = prog_language
class Teacher(My_Employee):
    def __init__(self, name, basic_salary, gender, age,subject,yearofteaching):
        super().__init__(name, basic_salary, gender, age)
        self.subject = subject
        self.yearofteaching = yearofteaching
class Hourly_Employee(My_Employee):
    def __init__(self, name, basic_salary, gender, age,hourly_rate,hours_worked):
        super().__init__(name, basic_salary, gender, age)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def hourly_employee_salary(self):
        hourly_employee_salary = self.basic_salary + (self.hourly_rate * self.hours_worked)
        return hourly_employee_salary

class BankAccount():
    def __init__(self, account_number,account_holder_name,account_type,account_balance,bank_name):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.account_balance = account_balance
        self.bank_name = bank_name
class Deposits(BankAccount):
    def __init__(self, account_number,account_holder_name,account_type,account_balance,bank_name):
        super().__init__()
    def deposit(self,deposit_amount):
        self.deposit_amount = deposit_amount
        deposit = (self.account_balance + self.deposit_amount)
        return deposit
    def withdraw(self, withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount
        if self.account_balance > 1:
            withdraw = (self.account_balance - self.withdrawal_amount )
            return withdraw
        else:
            print('You do not have enough money!')
