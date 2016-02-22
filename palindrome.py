def palidrome():
  print '*****************'
  print '**HELLO THERE!***'
  print '*****************'
  print '\n Welcome the the Python Palindrome Prober!\n'
  print """Please enter the word you would like to check
                              for example: racecar         """
  
  prompt = '>'
  
  word = raw_input(prompt )
  
  if word == word[::-1]:
      print 'Yes your word is a palindrome!'
  else:
      print 'Sorry this word isn\'t a palindrome :('
      
  print '\nHave a nice day!'
  
  re_play = raw_input("Want to play agian?")
  
  if re_play.lower() == "yes":
    palidrome()
  else:
    print "Your Loss!"
  
palidrome()   







