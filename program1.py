"""
this is first program to counte the number of vowels, words, sentences, and punctuation marks.
"""

from importlib.resources import contents
from string import punctuation



def count_vowels(test_Sentence):
    number_of_vowels=0
    """
    this function is used to count vowels
    Parameters:
                    test_sentence (str): stores sentence set by user or data read from a file

            Returns:
                   number_of_vowels (int) : returns count of vowels in sentence
    
    """
    for element in test_Sentence:
        if element=="a" or element=="e" or element=="i" or element=="o" or element=="u":
            number_of_vowels=number_of_vowels+1
    return number_of_vowels

def count_words(test_Sentence):
    
    """
    this function is used to count total number of words 
    Parameters:
                    test_sentence (str): stores sentence set by user or data read from a file
    
    """
    number_ofword=test_Sentence.split()
    print(len(number_ofword))


def count_puntuation_marks(sentence):
    number_of_punctuation_marks=0
    """
    this function is used to count punctuation marks
    Parameters:
                    sentence (str): stores sentence set by user or data read from a file

            Returns:
                   number_of_puntuations : returns count of punctuations in sentence
    
    """

    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for element in sentence:
        if element in punc:
            number_of_punctuation_marks+=1
    return number_of_punctuation_marks

print(" enter 1-)to read data from file")
print(" 2-) to take input")

choice = int(input("enter choice"))
if choice==2:
    sentence = input("enter meaningful sentence")
    count_of_vowels = count_vowels(sentence)
    print("number of vowels = " + str(count_of_vowels))    
    puntuation_marks = count_puntuation_marks(sentence)
    print("number of punctuation marks = " + str(puntuation_marks)) 
    count_words(sentence)
if choice==1:
    file = open("demo.txt")
    content = file.read()
    count_of_vowels = count_vowels(content)
    print("number of vowels = " + str(count_of_vowels))    
    puntuation_marks = count_puntuation_marks(content)
    print("number of punctuation marks = " + str(puntuation_marks)) 
    count_words(content)



