"""
Where the game is actually run
"""
import filter_words as fw
import compute_n_primes as cnp
from ScoreDict import ScoreDict
from Puzzle import Puzzle
import random as ran



if __name__ == "__main__":

    # Open the word list and character list for reading
    word_file = open("word_list.txt", 'r')
    alphabet_file = open("french_chars.txt", "r")
    # make the words into a list of words
    words = []
    alphabet = []
    for line in word_file:
        words.append(line.strip("\n"))
    for line in alphabet_file:
        alphabet.append(line.strip("\n"))

    # Get puzzle size
    n = int(input("How many letters is the puzzle:    "))
    
    # Now we get only words with less than or equal to n letters
    out = fw.filter_to_n_letters(n, words)
    words = out[0]

    n_letter_words = out[1]

    # Now we create the dictionary with the word scores
    # There are 41 unique characters in the french alphabet
    num_chars = len(alphabet)

    primes = cnp.compute_n_primes(num_chars)

    
    #print(words)
    scores = ScoreDict(alphabet, words, primes)
    

    # Wow we have the dictionary of words and scores filled in.
    # So we pick a random word from our n_letter_words then we make the puzzle class
    target_word = n_letter_words[ran.randint(0, len(n_letter_words))]
    target_letter = target_word[ran.randint(0, len(target_word))]
    valid_words = scores.get_valid_words(target_word, target_letter)
    
    puzzle = Puzzle(valid_words, target_word)


    #while we still have words to find in the puzzle
    while len(puzzle.words) > 0:
        print("The target word is:    " + target_word)
        print("The target letter is:    " + target_letter)
        print("\n")
        print("There are " + str(puzzle.get_num_words_remaining()) + " words remaining")
        # print(puzzle.words)
        guess = input("Guess a word:   ")
        if puzzle.is_correct_word(guess):
            print("Found a correct word \n")
        else:
            print("That is not a word \n")
        puzzle.display_found_words()

