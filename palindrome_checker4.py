# Main function
def palindrome_checker(word):
    init_word = word
    word = word.replace(' ', '')
    word1 = word[::-1]
    if word == word1:
        return 'The word {} is a palindrome!'.format(init_word)
    else:
        return 'The word {} is not a palindrome!'.format(init_word)

# Presentation
print('Welcome to our palindrome checker! \nEnter the word that you want to check:')
word = input()
print(palindrome_checker(word))
