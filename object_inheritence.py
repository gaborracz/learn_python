class PartyAnimal:
    x = 0
    name = ""
    
    def __init__(self, nam):
        self.name = nam
        print(self.name, " constructed..")
        
    def Party(self):
        self.x += 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
    points = 0
    
    def touchdown(self):
        self.points = self.points + 7
        self.Party()
        print(self.name, "points", self.points)

an = PartyAnimal("Jim")
aa = FootballFan("Dwight")

an.Party()
aa.touchdown()