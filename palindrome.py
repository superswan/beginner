""" Simple Program to Check Palindrome String"""

print(('*' * 18) + 'HELLO THERE!' + ('*' * 18) + '\n Welcome to the Python Palindrome Prober!\n')

def palidrome():

    print("Please enter the word you would like to check\nFor example: racecar")

    word = input(">> ").lower()

    print('Yes, your word is a palindrome!' if word == word[::-1] else 'Sorry, this word isn\'t a palindrome :(') # Checks if the string doesn't change when reversed

    print('\nHave a nice day!')

    if input('Want to play again (y/n)?').lower()[0] == 'y':
        palidrome()
    else:
        print("Your Loss!")

palidrome()


def harder_palindrome(word):
    """ Takes in a word, and does the palindrome step by step, using a loop"""
    """ makes the [::-1] notation clearer (hopefully)"""
    for i in range(len(word)//2): #you just want to check the first half and second half
        if (word[i] == word[-i-1]): #compare last and first until you reach the middle
            pass #do nothing
        else:
            return False #oopsy, not palindrome
    return True #yay

