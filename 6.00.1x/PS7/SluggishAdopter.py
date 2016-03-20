__author__ = 'ThanhNam'
import Adopter;

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.adopter_location = (float(location[0]),
                                 float(location[1]))
    def get_distance(self,adoption_center):
        import math
        tmp_location = adoption_center.get_location()
        distance = ((tmp_location[0] - self.adopter_location[0])**2)
        distance += ((tmp_location[1] - self.adopter_location[1])**2)
        return math.sqrt(distance)

    def get_score(self, adoption_center):
        import random as rand
        base_score = Adopter.get_score(self,adoption_center)
        distance = self.get_distance(adoption_center)
        if distance < 1.0:
            add_score = 1.0
        elif distance < 3.0 :
            add_score = rand.uniform(0.700,0.900)
        elif distance < 5.0 :
            add_score = rand.uniform(0.500,0.700)
        else:
            add_score = rand.uniform(0.100,0.500)
        return (base_score * add_score)
