__author__ = 'ThanhNam'
import string

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True

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


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'

    numberOfGuesses = 8
    guesses = []

    while numberOfGuesses > 0:
        print '-----------'
        print 'You have ' + str(numberOfGuesses) + ' guesses left'
        availableLetters = getAvailableLetters(guesses)
        print 'Available Letters: ' + availableLetters
        guess = raw_input("Please guess a letter: ")
        guess = guess.lower()

        if guess in guesses:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guesses)
        elif guess not in secretWord:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, guesses)
            numberOfGuesses -= 1
            guesses += guess
        else:
            guesses += guess
            print 'Good guess: ' + getGuessedWord(secretWord, guesses)

        if isWordGuessed(secretWord, guesses) == True:
            print '------------'
            print 'Congratulations, you won!'
            break

    if numberOfGuesses == 0:
        print '-----------'
        print 'Sorry, you ran out of guesses. The word was ' + secretWord


hangman('sadflkasfsalslakjflsafjkasf');