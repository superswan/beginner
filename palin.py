print ('*****************')
print ('**HELLO THERE!***')
print ('*****************')
print ('\nWelcome the the Python Palindrome Prober!\n')
print ('\nPalindrome is a a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam, noon or nurses run.\n')
        
def word_is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
def play_round():
    print ('''Please enter the word you would like to check
                              for example: armstrong''')
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
