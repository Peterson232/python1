#list
employees = ['Peter', 'John', 'Smith', 'Mike']
print(employees)
print(employees[2])
print(employees[1:4])
employees[0]= 'William'
print(employees)
employees.append('Susan')
print(employees)
employees.insert(2, 'koi')
print(employees)
employees.extend(['Uhuru', 'Ruto', 'Kasongo'])
print(employees)
#tuple
products = ('Banana', 'Apple','orange','pear')
print(products)
print(products[1])
print(products[1:3])

#set
students = {'Jeff', 'Samuel', 'Wanjez','Ann','Stacy'}
print(students)
students.add('Charles')
print(students)
students.update(['Ruben'])
print(students)
students.remove('Wanjez')
print(students)
#dictionary
person = {
    'Name' : 'Peter',
    'Email' : 'Peter@gmail.com',
    'Address' : 'Nairobi',
    'Gender' : 'Male'
}
print(person)
print(person['Gender'])
print(person['Name'])
person['Marital status'] = 'Single'
print(person)

if 'education' in person:
    print('yes it is present')
else:
    print('not present')

Phonestore ={
    'Phone_name' : 'Pear18',
    'screen size': '6.7 inch display',
    'storage size':'256 GB internal storage' ,
    'Ram size' : '12 GB RAM',
    'Processor' : 'Snapdragon 8 Gen2'
}
print(Phonestore)
if 'camera megapixel' in Phonestore:
    print('yes it is present')
else:
    print('not present')