import sys

class ZooKeeper: 
    def __init__(self):
        self.cleans_the_enclosures = "cleans"
        self.feeds_animals = "feeds"

class Enclosure:
    def __init__(self, animal_count, cleanliness_percentage, is_open):
        self.contains_animals = animal_count
        self.clean_dirty = cleanliness_percentage
        self.open_close = is_open

class Animal:
    def __init__(self, species, is_hungry, is_happy, is_loved):
        self.species = species
        self.isHungry = is_hungry
        self.isHappy = is_happy
        self.isLoved = is_loved

def main():
    zoo_keeper = ZooKeeper()
    enclosure = Enclosure(animal_count=12, cleanliness_percentage=50, is_open='opened')
    
    animals = [
        Animal(species='Lion', is_hungry='hungry', is_happy='happy', is_loved='loved'),
        Animal(species='Penguin', is_hungry='not hungry', is_happy='happy', is_loved='very loved'),
        Animal(species='Elephant', is_hungry='hungry', is_happy='not happy', is_loved='loved'),
    ]
    
    print('\n\nDo you want to see an example of a day in the zoo?\n\n')
    tell_a_day = input('[Y]es or [N]o: ').strip().upper()
    
    if tell_a_day == 'N':
        sys.exit()
    else:
        print('\n\nOkey... ... .. .\n\n')
        print(f'''At first at 8am our Zoo Keeper {zoo_keeper.cleans_the_enclosures} our enclosures and then {zoo_keeper.feeds_animals} all of the animals.
            In our zoo we have about {enclosure.contains_animals} animals and {enclosure.clean_dirty}% of them are dirty because doors are {enclosure.open_close}
            and they walk at night. 
            ''')
        
        for animal in animals:
            print(f"The {animal.species} is {animal.isHungry} and is {animal.isHappy}. It is {animal.isLoved} by people.")

if __name__ == '__main__':
    main()
