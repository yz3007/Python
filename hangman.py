# Name: Yufei
# Section:
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist


# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0, len(words_dict))]
    return word


# end of helper code
# -----------------------------------




# CONSTANTS
#MAX_GUESSES = 6

# GLOBAL VARIABLES
# secret_word = 'claptrap'

letters_guessed = []


# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    ls = list()
    for i in secret_word:
        if i not in letters_guessed:
            ls.append('-')
        else:
            ls.append(i)
    return join(ls, '')


def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed

#    global MAX_GUESSES  # add by myself

    # Put the mistakes_made variable here, since you'll only use it in this function

    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word = get_word()
#    print MAX_GUESSES, 'guesses left'
    print print_guessed()
    print_hangman_image(mistakes_made)

    while True:

        word = raw_input('Please enter a letter/ a full word(trick: guess): ')
        word = word.lower()

        # for  one-time spell all of letters
        if word == 'guess':
            hit = raw_input('Now you can enter the entire word but you will be punished by dying fast if you fail:\n')
            if secret_word == hit:
                print 'Success:', secret_word
            else:
                mistakes_made += 2
                if mistakes_made >= 6:
                    print_hangman_image(6)
                    break
                print_hangman_image(mistakes_made)
                continue


        if word in letters_guessed:
#            MAX_GUESSES -= 1
#            print MAX_GUESSES, 'guesses left (caused by repetition)'
            print 'Please enter different letter due to repetition'
            continue
        else:
#            MAX_GUESSES -= 1
            letters_guessed.append(word)

            print print_guessed()

            if word_guessed():
                break

            if word not in secret_word:
                mistakes_made += 1
                print_hangman_image(mistakes_made)

#            print MAX_GUESSES, 'guesses left'

            if mistakes_made >= 6:
                break


    print 'Secretwords:', secret_word
    return None


play_hangman()
