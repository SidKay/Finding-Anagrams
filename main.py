# A simple program that checks if two words are anagrams
# Made by Obinna Anya for the Zuri Internship Program

# How this program works is by receiving input from the user, 
# counts the letters used in each word by assigning the number of letters in a dictionary, and
# then compares the dictionary of letters for each word


def find_anagrams(word1, word2):
    # Checks if the words are the same length
    if len(word1) != len(word2):
        return False
    
    # Create a dictionary for the letters used in each word
    alphabet1 = {
            "a" : 0, 
            "b" : 0,
            "c" : 0,
            "d" : 0,
            "e" : 0,
            "f" : 0,
            "g" : 0,
            "h" : 0,
            "i" : 0,
            "j" : 0,
            "k" : 0, 
            "l" : 0, 
            "m" : 0, 
            "n" : 0, 
            "o" : 0, 
            "p" : 0, 
            "q" : 0, 
            "r" : 0, 
            "s" : 0, 
            "t" : 0, 
            "u" : 0, 
            "v" : 0, 
            "w" : 0, 
            "x" : 0, 
            "y" : 0, 
            "z" : 0,
            " " : 0
        }

    alphabet2 = {
            "a" : 0, 
            "b" : 0,
            "c" : 0,
            "d" : 0,
            "e" : 0,
            "f" : 0,
            "g" : 0,
            "h" : 0,
            "i" : 0,
            "j" : 0,
            "k" : 0, 
            "l" : 0, 
            "m" : 0, 
            "n" : 0, 
            "o" : 0, 
            "p" : 0, 
            "q" : 0, 
            "r" : 0, 
            "s" : 0, 
            "t" : 0, 
            "u" : 0, 
            "v" : 0, 
            "w" : 0, 
            "x" : 0, 
            "y" : 0, 
            "z" : 0,
            " " : 0
        }

    # Counts the letters used in each word and assigns it to the "alphabet" dictionary        
    for letter in word1:
        alphabet1[letter] += 1
    
    for letter in word2:
        alphabet2[letter] += 1

    # Compares the dictionary of letters for word1 and word2 if they are the same
    if (alphabet1 != alphabet2):
        return False
    else:
        return True

firstWord = input("Enter a word: ")
secondWord = input("Enter another word: ")
print(find_anagrams(firstWord, secondWord))