print('*****************')
print('**HELLO THERE!***')
print('*****************')
print('\nWelcome the the Python Palindrome Prober!\n')

def palindrome():

    print('''Please enter the word you would like to check
            for example: racecar''')

    word = str(input(">> "))

    if word == word[ : : -1]:
        print("Yes, your word is a palindrome!")
    else:
        print("Sorry this word isn't a palindrome :(")

    re_play = input("Want to play again (y/n)? ")

    if re_play.lower().startswith("y"):
        palindrome()
    else:
        print('\nHave a nice day!')

palindrome()
