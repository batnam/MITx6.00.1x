__author__ = 'ThanhNam'
import Adopter;

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        if str(type(allergic_species)) == "<type 'str'>" :
            self.allergic_species = [allergic_species]
        else:
            self.allergic_species = allergic_species
    def get_score(self, adoption_center):
        base_score = Adopter.get_score(self,adoption_center)
        add_score = 1
        for animal in self.allergic_species:
            if( adoption_center.get_number_of_species(animal) > 0):
                add_score = 0.0
                break
        return (base_score * add_score)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species,medicine_effectiveness):
        AllergicAdopter.__init__(self,name, desired_species,allergic_species)
        if str(type(medicine_effectiveness)) == "<type 'str'>" :
            self.medicine_effectiveness = [medicine_effectiveness]
        else:
            self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        base_score = Adopter.get_score(self,adoption_center)
        add_score = 1.0
        allergic_adoption = []
        for animal in self.allergic_species:
            if( adoption_center.get_number_of_species(animal) > 0):
                allergic_adoption.append(animal)
        for animal in  allergic_adoption:
            try :
                me_score = self.medicine_effectiveness[animal]
            except :
                me_score = 0
            if me_score < add_score :
                add_score = me_score
        return (base_score * add_score)
