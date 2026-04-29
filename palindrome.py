""" Simple Program to Check Palindrome String"""

print(('*' * 18) + 'HELLO THERE!' + ('*' * 18) + '\n Welcome to the Python Palindrome Prober!\n')

def palidrome(word):
    ch="y"
    while ch=="y":# checks until ch is y 
        
        print(f"Yes, your {word} is a palindrome!" if word.lower() == word[::-1].lower() else f"Sorry,{word} isn't a palindrome" ) # Checks if the string doesn't change when reversed
        print('\nHave a nice day!\n')

        ch=input("Do you want to run the program again (Y/N)?  ").lower() #update the ch
    return "Exited"
     

string=input("Enter the word :   ")
print(palidrome(string))


