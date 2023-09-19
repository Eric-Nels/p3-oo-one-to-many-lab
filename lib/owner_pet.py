class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f'Invalid pet type: {pet_type}')
        else:
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            Pet.all.append(self)


class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if pet in Pet.all:
            pet.owner = self
        else:
            raise Exception(f'Invalid pet: {pet}')
        
    def get_sorted_pets(self):
        owner_pets = self.pets()
        sorted_pets = sorted(owner_pets, key= lambda pet: pet.name)
        return sorted_pets