#Introduction of Program to User
print ('*****************')
print ('**HELLO THERE!***')
print ('*****************')
print ('Welcome the the Python Palindrome Prober!')
print ('Palindrome is a a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam, noon or nurses run.')
#Program understands if the word inputted is a palindrome        
def word_is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
#Inputs user for a word and answers if it is a palindrome
def play_round():
    print ('''Please enter the word you would like to check
                              for example: racecar''')
    word = input(">> ")
    
    if word_is_palindrome(word):
        print ('Yes, your word is a palindrome!')
    else:
        print ("Sorry this word isn't a palindrome :(")
#If user wishes to continue; if not, the game will discontinue
def keep_playing():
    re_play = input("Want to play again (y/n)? ")
    if re_play.lower().startswith("y"):
        return True
    else:
         print ('Have a nice day!')
         return False
#Program will run as long as user indicates so
play_round()
while keep_playing():
    play_round()
