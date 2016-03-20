__author__ = 'ThanhNam'
# Enter your code for the Adopter class here
class Adopter:#(object):
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        # name- A string that represents the name of the adopter
        # desired_species- A string that represents the desired species to adopt
        self.name = name
        self.desired_species = desired_species
        #print "Adopter Initialized"
    def get_name(self):
        # Returns the name of the adopter
        return self.name
    def get_desired_species(self):
        # Returns the desired species of the adopter
        return self.desired_species
    def get_score(self, adoption_center):
        # For the base Adopter class, this score will be 1 * num_desired
        # where num_desired is the number of the adopter's desired species
        # that the adoption center has.
        return (1.0 * adoption_center.get_number_of_species(self.desired_species))