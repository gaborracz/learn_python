class PartyAnimmal:
    
    x = 0
    
    def __init__(self):
        print("PartyAnimal is constructed.")
    
    def party(self):
        self.x += 1
        print(f"So far {self.x}")
    
    def __del__(self):
        print(f"PartyAnimal is destructed. self.x is: {self.x}")
        
class AnotherAnimal:
    
    x = 0
    name = ""
    
    def __init__(self, z):
        print("AnotherAnimal is constructed...")
        self.name = z   

    def party(self):
        self.x += 1
        if self.x > 3:
            print(f"{self.name} is partying real hard....")
        else:
            print(f"{self.name} is partying...")


an = PartyAnimmal()

# print("This is the type of an : ", type(an))
# print("This is the dir of an : ", dir(an))

aa = AnotherAnimal("Jim")
aa.party()
aa.party()
aa.party()
aa.party()
aa.party()
# print("\n\nThis is the type of aa : ", type(an))
# print("This is the dir of aa : ", dir(an))