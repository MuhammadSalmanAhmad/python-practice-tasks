"""
this is first program to counte the number of vowels, words, sentences, and punctuation marks.
"""
import string
def print_details(vowels,punctuations,words):
    """
    this function is used to print vowels and punctuations in a sentence
    Parameters:
           vowels (int) : recieves value of vowels as parameter from main
           punctuations (int) : recieves count of punctuation marks as parameter from main
    returns :
           nothing
    """
    print("number of vowels = {}".format(vowels))
    print("number of punctuation marks  = {}".format(punctuations))
    print("number of words = {}".format(len(words)))

def count_vowels(test_sentence):
    """
    this function is used to count vowels
    Parameters:
            test_sentence (str): stores sentence set by user or data read from a file
    Returns:
            number_of_vowels (int) : returns count of vowels in sentence
    """
    number_of_vowels = 0
    vowels = ["a","e","i","o","u"]
    for element in test_sentence:
        if element in vowels:
            number_of_vowels=number_of_vowels+1
    return number_of_vowels

def count_words(test_sentence):
    """
    this function is used to count total number of words
    Parameters:
            test_sentence (str): stores sentence set by user or data read from a file
    returns :
            number_of_words (list) : contains list of words in a sentence
    """
    number_of_words = test_sentence.split()
    return number_of_words

def count_puntuation_marks(sentence):
    """
    this function is used to count punctuation marks
    Parameters:
           sentence (str): stores sentence set by user or data read from a file
    Returns:
          number_of_puntuations : returns count of punctuations in sentence
    """
    number_of_punctuation_marks=0
    for element in sentence:
        if element in string.punctuation:
            number_of_punctuation_marks+=1
    return number_of_punctuation_marks

def main():
    """
    this is the main module of the program all global and defualt run is defined over here
    """
    print(" enter 1-)to read data from file")
    print(" 2-) to take input")
    choice = int(input("enter choice"))
    if choice==2:
        sentence = input("enter meaningful sentence")
        count_of_vowels = count_vowels(sentence)
        punctuation_marks = count_puntuation_marks(sentence)
        words_list=count_words(sentence)
        print_details(count_of_vowels,punctuation_marks,words_list)
    if choice==1:
        filename = input('enter filename with proper path like "D:\\myfiles\\welcome.txt"')
        file = open(filename.strip())
        content = file.read()
        count_of_vowels = count_vowels(content)
        punctuation_marks = count_puntuation_marks(content)
        words_list = count_words(content)
        print_details(count_of_vowels,punctuation_marks,words_list)
if __name__ == "__main__":
    main()
