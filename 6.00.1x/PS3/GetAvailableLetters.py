__author__ = 'ThanhNam'
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a = string.ascii_lowercase
    myString = ''

    for letter in a:
        if letter not in lettersGuessed:
            myString += letter

    return myString