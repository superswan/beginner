""" Simple Program to Check Palindrome String"""

print('*' * 16)
print('**HELLO THERE!**')
print('*' * 16)
print('\n Welcome the the Python Palindrome Prober!\n')

def palidrome():

    print("Please enter the word you would like to check\nFor example: racecar")

    word = input(">> ").lower()

    if word == word[::-1]:							#Checks if the string doesnt change when reversed				
        print('Yes, your word is a palindrome!')
    else:
        print('Sorry, this word isn\'t a palindrome :(')

    print('\nHave a nice day!')

    re_play = input("Want to play again (y/n)?").lower()

    if re_play[0] == 'y':
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

