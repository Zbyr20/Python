#Class

class Person:
     
    #class attributes
    address = "No ınfo"

    #constructer
    def __init__(self, name, year):
        #object attributes
        self.name = name
        self.year = year
        print("Constructer Çalıştı")

    #methods
#object(instance)

p1 = Person(name="Zübyr",year=12)
p2 = Person(name="Zübyr",year=12)
#Updating
p1.address = "Diyarbakır"
#accessing object
print(f"p1: name : {p1.name} year: {p1.year} address: {p1.address}")
print(f"p2: name: {p2.name} year: {p2.year} address: {p2.address}")

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)