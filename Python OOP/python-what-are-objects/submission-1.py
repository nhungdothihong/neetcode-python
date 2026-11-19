class Pet:
    def __init__(self,name, species, hunger, energy):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)
print(f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")