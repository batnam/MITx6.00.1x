__author__ = 'ThanhNam'
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    length = len(secretWord)
    string = []
    realString = ''
    for i in range(length):
        string += '_'

    for letters in range(length):
        for guesses in lettersGuessed:
            if secretWord[letters] == guesses:
                string[letters] = guesses

    for letters in string:
        if letters == '_':
            realString += letters + ' '
        else:
            realString += letters
    return realString