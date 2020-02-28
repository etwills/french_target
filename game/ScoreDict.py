
class ScoreDict:
    """
    Initalises the library of scores
    Conditions:
    - Alphabet and primes have the same length
    - 
    """
    def __init__(self, alphabet, words, primes):
        self.word_scores = {}
        self.letter_scores = {}
        self.word_list = words
        self.primes = primes
        self.alphabet = alphabet
        self.make_letter_scores()
        self.make_word_scores()
        # self.target_letter = target_letter
        # self.target_letter_score = self.letter_scores[target_letter]
    
    def make_letter_scores(self):
        for i in range(len(self.alphabet)):
           # We go through and map each letter in our alphabet to a prime number
           self.letter_scores[self.alphabet[i]] = self.primes[i]
    
    def make_word_scores(self):
        for word in self.word_list:
            # compute the score for a word
            score = self.compute_score(word)
            # store the score in the dictionary with word as the key
            self.word_scores[word] = score
    
    
    def compute_score(self, word):
        score = 1
        for letter in word:
            # we create a product of the letter scores for each word
            try:
                score *= self.letter_scores[letter]
            except KeyError:
                pass
        return score

    """
    Takes 
    w: a word and returns the words that can be made using a subset of the letters from w 
    l: a letter in w that is the target letter
    """
    def get_valid_words(self, w, l):
        valid_words = []
        w_score = self.word_scores[w]
        l_score = self.letter_scores[l]
        # go through the key value pairs to find which the words we are looking for
        for word, score in self.word_scores.items(): 
            # if our score is less than or equal to our w_score it might be a divisor
            if score <= w_score:
                # if score divides w_score it is a word we are looking for
                if w_score % score == 0:
                    # now if it contains the target letter it is a word we want
                    if score % l_score == 0:
                        valid_words.append(word)

        return valid_words
    

    