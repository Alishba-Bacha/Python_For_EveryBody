class PartyAnimal:      #Class is reserved word
    x = 0
    name = ""
    def __init__(self):       #Constructor often used for initialization of values
        print("I am constructed")

    def party(self):
        self.x = self.x +1        #Each class has a bit of code
        print("Num: ", self.x)

    def __del__(self):
        print("I am destructed", self.x)
    
an = PartyAnimal()    #construct object and store in a variable   and moment of construction
an.party()         #Tell the object to run code in class work as PartyAnimal.party(an)
an.party()
an.party()
print("Dir", dir(an))     # tell the fuctions of class
print("Type", type(an))    #Tell something about object
an = 42
print("an contains", an)

#Object Inheritance
class Party_Animal:
    x = 0
    name = ""

    def __init__(self, z):  #A constructor with a para meter z which itself is a particular object
        self.name = z
        print("Name:", self.name)
    
    def party(self):
        self.x = self.x +1        
        print("count: ", self.x)

class FootBall(Party_Animal):           #Child class of Party animal
    points = 0
    def touchDown(self):
        self.points =self.points + 7
        self.party()
        print(self.name, "Self points:", self.points)

p = Party_Animal("Anmol") #Anmol is the particular instance/object for specified constructor
p.party()
x = FootBall("Anmol")
x.party()
x.touchDown()