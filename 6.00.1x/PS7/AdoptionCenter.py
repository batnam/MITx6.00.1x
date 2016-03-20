__author__ = 'ThanhNam'
# Enter your code for the AdoptionCenter class here
# Be sure to include the __init__, get_name, get_species_count, get_number_of_species, and adopt_pet methods.
class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method
    to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        # name- A string that represents the name of the adoption center
        # location - A tuple (x, y) That represents the x and y as floating
        #               point coordinates of the adoption center location.
        # species_types- A string:integer dictionary that represents the number
        #                   of specific pets that each adoption center holds.
        self.name = name
        self.location = (float(location[0]), float(location[1]))
        self.species_types = species_types.copy()
    def get_number_of_species(self, species):
        # Returns the number of a given species that the adoption center has.
        try :
            return self.species_types[species]
        except :
            return 0
    def get_location(self):
        # Returns location of the adoption centre
        return self.location
    def get_species_count(self):
        # Returns a copy of the full list and count of the available species
        #   at the adoption center.
        return self.species_types.copy()
    def get_name(self):
        # Returns name of center
        return self.name
    def adopt_pet(self, species):
        # Decrements the value of a specific species at the adoption center
        #   and does not return anything.
        if (self.species_types[species]) > 1 :
            self.species_types[species] -= 1
        else :
            self.species_types.pop(species)
        return None