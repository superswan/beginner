#To check whether the word is a palindrome

#Inputs to user what word they would like to process
c=input("Enter the word you want to check: ")
#If word matches a palindrome's requirements, it is a palindrome
if(c==c[::-1]):
        print("The word is a palindrome")
#If word does not match a palindrome's requirements, it is not a palindrome
else:
        print("The word is not a palindrome")
