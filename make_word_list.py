"""
Makes a list of all the words with no repeats

Needs to read al the data from the excel file then clean it up
"""

import pandas as pd


def read_data(filename):
    # open the right column of the excel file and make a list of all the words
    
    
    df = pd.ExcelFile(filename).parse('Lexique383') #you could add index_col=0 if there's an index
    x=[]
    x.append(df['3_lemme'])
    return x

"""
turn the list of words into a text file
"""
def word_list_to_text(words, out_text):
    
    f = open(out_text, "w")
    for i in range(len(words) - 1):
        try:
            f.write(words[i] + "\n")
        except TypeError:
            print(words[i])
    f.close()


"""
Takes a list of words and deletes any words appearing multiple times
"""
def delete_multiple_words(word_list):
    # split the list where you encounter new lines
    word_set = set()   
    # split based on the white spaces and get the word out of the end
    for i in range(len(word_list) - 1):
        word_set.add(word_list[i])
    
    return list(word_set)

"""
Removes the white spaces from words
"""  
def clean_white_space(item):
    x = item.split(" ")
    return x.last()



if __name__ == '__main__':
    filename = "/Users/Ethan/Documents/french_word_game/Lexique383/Lexique383.xlsx"

    words = read_data(filename)
    print(words[0][1], len(words[0][1]))
    print(type(words[0][1]))
    # clean all the junk off each word
    # words = clean_words(words[0])
    # turn the list into a text file
    words = delete_multiple_words(words[0])
   


    word_list_to_text(words, "out.txt")

    




    

