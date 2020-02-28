"""
The main puzzle class that deals with what words have been found and what words still need to be found
"""

class Puzzle:
    """
    words: a set of words
    target_word: a nine letter word we are looking for
    """
    def __init__(self, words, target_word):
        self.target_word = target_word
        self.words = words
        self.found_words = set()
    
    def display_found_words(self):
        print("You have found " + str(len(self.found_words)) + " words")
        for word in self.found_words:
            print(word)
    
    def is_correct_word(self, guess):
        if guess in self.words:
            self.add_to_found(guess)
            self.remove_from_words(guess)
            return True
        else:
            return False

    def add_to_found(self, word):
        self.found_words.add(word)

    def remove_from_words(self, word):
        print(self.words, word)
        self.words.remove(word)

    def get_num_words_remaining(self):
        return len(self.words)