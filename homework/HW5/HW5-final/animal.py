# Problem 1
class Animal:

    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    def __init__(self, name, species):
        self.name = name
        self._species = species

    def __repr__(self):
        return f'{self.name} ({self._species})'
    
    @property  #decorator
    #getter is printing out the new value
    def species(self):
        return self._species
    
    @species.setter
    # this is changing the value if needed
    def species(self,into):
        assert into in Animal.valid_species, Exception(f'invalid species: {into}') # checking to see if its in the list
        self._species = into
    

if __name__ == '__main__':
    dog = Animal('Fido', 'dog')
    print(dog.species)

    dog.species = 'cat'
    print(dog.species)

    dog.species = 'TheThing'
    print(dog.species)
