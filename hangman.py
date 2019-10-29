import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek listremaining lives hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if get_guessed_word(secret_word, letters_guessed) == secret_word:
        return True


    return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

   
    guessed_word = ""
    for index in secret_word:
        if index in letters_guessed:
            guessed_word += index
        else:
            guessed_word += "_"
    
    return guessed_word
def invalid(letters):
    if len(letters) > 1: #and letters == type(int):
        return False
    if not letters.isalpha():
        return False
    else:
        return True
   # return sum

def get_hint(secret_word,letters_guessed):
    import random

    letter_list=[]
    for index in secret_word:
        if index not in letters_guessed:
            if index not in letter_list:
                letter_list.append(index)
    letter=random.choice(letter_list)
    return letter

def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    # import string
    all_letters_left = string.ascii_lowercase
    print all_letters_left
    letter_left=""
    for letter in all_letters_left:
        if letter not in letters_guessed:
            letter_left=letter_left+letter
    return letter_left

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""

    letters_guessed = []
    USER_INPUT=raw_input("which level you want to play \n(a). Easy \n (b). Medium \n (c) Hard ")
    USER_INPUT=USER_INPUT.lower()
    if USER_INPUT == "c":
        image=0
        images=[IMAGES[1],IMAGES[5],IMAGES[6],IMAGES[7]]
        remaining_lives=4
    elif  USER_INPUT =="b":
        image=0
        images=[IMAGES[2],IMAGES[3],IMAGES[4],IMAGES[5],IMAGES[6],IMAGES[7]]
        remaining_lives=6
    elif USER_INPUT == "a":
        remaining_lives=8
        images=[IMAGES[0],IMAGES[1],IMAGES[2],IMAGES[3],IMAGES[4],IMAGES[5],IMAGES[6],IMAGES[7]]
        image=0
    while remaining_lives>0:
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + str(available_letters)
        
        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()

        if letter == "hint":
            letter = get_hint(secret_word,letters_guessed)
            print "your guess is this =" , letter
            letters_guessed.append(letter)

            print get_guessed_word(secret_word, letters_guessed)
            print " "

        if not invalid(letter):
            print "this letter is not right "
            continue


        elif letter in secret_word:

            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""
            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break

        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            print "remaining_lives is=" ,remaining_lives
            print images[image]

            print ""
            remaining_lives=remaining_lives-1 
            image=image+1 
    print "Oops you lose this game " 
    print "your secret word is this = " , secret_word 
            
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)    