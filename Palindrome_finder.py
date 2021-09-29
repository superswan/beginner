#Program to check if a word is a palindrome...using OOP.
class PalindromeString(str):
    """This class IS-A string. That means inherits from Python's string object."""
    def is_palindrome(self):
        """Calling this method on a string determines if a string is a palindrome by returning true if it is and false otherwise."""
        self = self.replace(' ','')
        return self.lower() == self[::-1].lower()

if __name__=='__main__':#makes the following code not run if this module is imported
    duration = None
    while duration == None:
    	try:
    		duration=int(input("How many words do you want to input?\n"))
    	except ValueError:
    		print( "Plese input a valid decimal number.")
    		
    number_of_times = 0
    while number_of_times < duration:
        word= input("What is your word?\n")
        word=PalindromeString(word)
        if word.is_palindrome():
            print("This word is a Palindrome")
        else:
            print("This word isn't a palindrome")
        number_of_times += 1