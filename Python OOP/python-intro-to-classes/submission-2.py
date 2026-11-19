class Pet:
    def __init__(self, name, species):
        self.name = name 
        self.species = species 
        
pet = Pet("Fluffy", "cat")
print(f"My pet is a {pet.species} named {pet.name}")