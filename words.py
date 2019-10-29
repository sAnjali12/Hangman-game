import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    my_data=open("words.txt","r")
    #Data=my_data.read()

    #my_file=my_data.load()
    my_files=my_data.readlines()
    Type=""

    for line in my_files:
        Type = line.split(" ")
    return Type
# print load_words()

def choose_word():

    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
print choose_word()
#  list1 = ['1', '2', '3']
# str1 = ''.join(list1)
# print str1