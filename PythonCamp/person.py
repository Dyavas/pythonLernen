class Person:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName


benutzer1 = Person("Ahmet,", "Yilmaz")
benutzer2 = Person("Davut,", "Yavas")
benutzer3 = Person("Ahmet,", "efe")

print(benutzer1.name, "", benutzer1.lastName)
print(benutzer2.name, "", benutzer2.lastName)
print(benutzer3.name, "", benutzer3.lastName)
