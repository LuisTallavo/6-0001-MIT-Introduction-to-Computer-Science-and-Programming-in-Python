# Problem Set 2, hangman.py
# Name: Luis Tallavo

# Hangman Game
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()


def brutesearch(lst, letter, position):
    remaining_words = []
    for i in lst:
        if len(i) > position:
            if i[position] == letter.lower():
                remaining_words.append(i)
    return remaining_words

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = wordlist
    position = -1

    for i in my_word:
        if i != ' ':
            position = position + 1
        if i != '_' and i != ' ':
            possible_matches = brutesearch(possible_matches, i, position)

    for i in possible_matches:
         print(i)
    pass


def is_word_guessed (secret_word, letters_guessed):
    tracker = False
    for i in secret_word:
        if i in letters_guessed:
            tracker = True
        else:
            return False
    return tracker

def get_guessed_word (secret_word, letters_guessed):
    guessedstring = ''
    for i in secret_word:
        if i in letters_guessed:
            guessedstring = guessedstring + i
        else:
            guessedstring = guessedstring + '_ '
    return guessedstring    

def get_available_letters (letters_guessed):
    available_letters = string.ascii_lowercase
    for i in letters_guessed:
        for j in available_letters:
            if i == j:
                available_letters = available_letters.replace(i, '')
    return available_letters

def hangman(secret_word):
    guesses = 6
    uniques = ''
    unique_letters = 0
    
    for i in secret_word:
        if i not in uniques:
            uniques = uniques + i
            unique_letters = unique_letters + 1
    
    letters_guessed = ''

    warnings = 3
    
    print("The secret word contains: " + str(len(secret_word)) + " letters")
    print('You have ' + str(guesses) +  ' guesses')  
    print('Available letters: ' + str(get_available_letters(letters_guessed)))
    print('------------------------------------------------')

    while guesses > 0:
        userguess = input('Please guess a letter: ')
        while not (userguess in string.ascii_lowercase or userguess in string.ascii_uppercase):
            if (userguess == '*'):
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------')
                break
            else: 
                warnings = warnings - 1
                if warnings > 0:
                    print('You have ' + str(warnings) +  ' remaining warnings')
                    print('------------------------------------------------')
                    userguess = input('Please guess a letter: ')
                elif warnings <= 0:
                    if guesses <= 1:
                        guesses = guesses - 1
                        break
                    else:
                        guesses = guesses - 1
                        warnings = 3
                        print('You have lost a guess! You have ' + str(guesses) + ' guesses remaining')
                        print('------------------------------------------------')
                        userguess = input('Please guess a letter: ')
        if guesses == 0:
            break
        letters_guessed = letters_guessed + userguess.lower()
        print(get_guessed_word(secret_word, letters_guessed))

        if (userguess.lower() in secret_word):
            print('Good guess!: ' + str(get_available_letters(letters_guessed)))
        else:
            if (userguess != '*'):
                guesses = guesses - 1
                print('Poor guess!: ' + str(get_available_letters(letters_guessed)))

        
        print('You have ' + str(guesses) +  ' remaining guesses')
        print('------------------------------------------------')
        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses * unique_letters
            print("YOU WIN! your score is: " + str(total_score))
            break
    if guesses == 0:
        print("You have lost the game!")
        print('------------------------------------------------')
    
if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)

