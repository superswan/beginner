print ('*****************')
print ('**HELLO THERE!***')
print ('*****************')
print ('\nWelcome the the Python Palindrome Prober!\n')
        
def word_is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
def play_round():
    print ('''Please enter the word you would like to check
                              for example: racecar''')
    word = input(">> ")
    
    if word_is_palindrome(word):
        print ('Yes, your word is a palindrome!')
    else:
        print ("Sorry this word isn't a palindrome :(")
        
def keep_playing():
    re_play = input("Want to play again (y/n)? ")
    if re_play.lower().startswith("y"):
        return True
    else:
         print ('\nHave a nice day!')
         return False
        
play_round()
while keep_playing():
    play_round()
