class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        self.hunger -= 1
        pass

# Create a pet
my_pet = Pet("Fluffy")

print(f"{my_pet.name}'s hunger level: {my_pet.hunger}")