__author__ = 'ThanhNam'
import Adopter;
class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        if str(type(considered_species)) == "<type 'str'>" :
            self.considered_species = [considered_species]
        else:
            self.considered_species = considered_species
    def get_score(self, adoption_center):
        base_score = Adopter.get_score(self,adoption_center)
        add_score = 0
        for animal in self.considered_species:
            add_score += adoption_center.get_number_of_species(animal)
        return (base_score + (0.3 * add_score))

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        if str(type(feared_species)) == "<type 'str'>" :
            self.feared_species = [feared_species]
        else:
            self.feared_species = feared_species
    def get_score(self, adoption_center):
        base_score = Adopter.get_score(self,adoption_center)
        add_score = 0
        for animal in self.feared_species:
            add_score += adoption_center.get_number_of_species(animal)
        base_score -= 0.3 * add_score
        if base_score < 0.0:
            base_score = 0.0
        return (base_score)