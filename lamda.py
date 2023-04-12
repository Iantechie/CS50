#applying decorators to sort a list containing dictionaries

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# def f(people):
#     return people['name']

# new = people.sort(key=f)
##OR USE LAMBDA 
people.sort(key=lambda person: person['name'])

print(people)