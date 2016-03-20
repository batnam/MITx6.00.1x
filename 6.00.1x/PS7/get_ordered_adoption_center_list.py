__author__ = 'ThanhNam'
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the
    scores for each AdoptionCenter to the Adopter will be ordered from highest
    score to lowest score.
    """
    # Create a list of list with respect to adoption centre and its score
    score_list = [[ac,adopter.get_score(ac)]
                  for ac in list_of_adoption_centers]
    # Sort the list based on score(high to low) and on alphabetical order
    # in event of tie
    score_list = sorted(score_list, key=lambda x: (-x[1], x[0].get_name()))
    # From sorted list extract list of adoption centres
    score_list = [item[0] for item in score_list]
    return score_list

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from
    list_of_adopters (in numerical order of score)
    """
    # Create a list of list with respect to adopter and its score
    score_list = [[ad, ad.get_score(adoption_center)]
                  for ad in list_of_adopters]
    # Sort the list based on score(high to low) and on alphabetical order
    # in event of tie
    score_list = sorted(score_list, key=lambda x: (-x[1], x[0].get_name()))
    # From sorted list extract list of adoption centres
    score_list = [item[0] for item in score_list]
    return(score_list[0:n])
