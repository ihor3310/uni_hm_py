import sys

class ZooKeeper: 
    def set_data(self, first, second):
        self.cleans_the_enclosures = first
        self.feeds_animals = second
class Enclosure:
    def set_data(self, first, second, third):
        self.contains_animals = first
        self.clean_dirty = second
        self.open_close = third
class Animals:
    def set_data(self, first, second, third):
        self.isHungry = first
        self.isHappy = second
        self.isLoved = third

ZooKeeper = ZooKeeper()
ZooKeeper.set_data('cleans', 'feeds')
Enclosure = Enclosure()
Enclosure.set_data(12, 50, 'opened')
Animals = Animals()
Animals.set_data('hungry', 'happy', 'loved')

def main():
    print('\n\nDo you want to see an example of a day in zoo?\n\n')
    tell_a_day = input('[Y]es or [N]o: ')
    if tell_a_day == 'N':
        sys.exit()
    else:
        print('\n\nOkey... ... .. .\n\n')
        print(f'''At first at 8am our Zoo Keeper {ZooKeeper.cleans_the_enclosures} our enclosures and then {ZooKeeper.feeds_animals} all of the animals.
            In our zoo we have about {Enclosure.contains_animals} animals and {Enclosure.clean_dirty}% of them are dirty because doors are {Enclosure.open_close}s 
            and they walk at night. All of animals are always {Animals.isHungry} and {Animals.isHappy}. Only penguins are most {Animals.isLoved} by people''')
if __name__ == '__main__':
    main()
