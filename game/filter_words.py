

"""
Takes the list of all words and reduces it to a list of n letter words

"""
import re

def filter_to_n_letters(num_letters, word_list):
    new_words = []
    n_letters = []
    for word in word_list:
        if len(word) <= num_letters:
            new_words.append(word)
            if len(word) == num_letters:
                n_letters.append(word)

    return [new_words, n_letters]

def remove_strange_chars(word_list):
    new_words = []
    regex = re.compile('[ -.@_!#$%^&*()<>?/\|}{~:"]')
    for word in words:
        if(regex.search(word) == None): 
            new_words.append(word)
        else: 
            print(word)
            print("\n")
    return new_words

if __name__ == "__main__":
    word_file = open('/Users/Ethan/Documents/french_word_game/game/out.txt', 'r+')
    words = []
    for line in word_file:
        words.append(line.strip("\n"))
    # now we have all the words cleaned
    print(words)
    words = remove_strange_chars(words)
    word_file.seek(0)
    for word in words:
        word_file.write(word + "\n")
    word_file.truncate()
    word_file.close()


 






    