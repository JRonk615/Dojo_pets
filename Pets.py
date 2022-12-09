# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method


class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self, distance):
        self.pet.play(distance)
    
    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.bathe.noise()


class Pet:

    def __init__(self, pet_name, type, tricks, health, energy):
        
        
        self.pet_name = pet_name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def play(self, distance):

        if distance > self.energy:
            print(f'{self.pet_name} seems too tired to walk that far')
        else:
            self.energy -= distance
            print(self.energy)
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.energy, self.health)
    
    def noise(self):
        print('bark bark')
    
    def sleep(self):
        self.energy += 25

class Doberman(Pet):
    def __init__(self, pet_name, type, tricks, health, energy):
        super().__init__(pet_name, type, tricks, health, energy)









