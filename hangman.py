import turtle
import random 
"""
class Drawings():
  
  jim = turtle.Turtle() #Remember the capital T
  jim.speed(5) #A speed of 0 makes him go as fast as possible

  arm_length = 100 #Change these if you want
  leg_length = 120

  def reset(self,jim): #reset sends him back to the center
    jim.pu() #pu is short for penup. Either work, you can use them interchangeably
    jim.setpos(0,0)
    jim.pd() #pd is short for pendown

  #head
  def head(self,jim):
    jim.seth(90) #seth is short for set_heading, and it changes the direction jim is facing.
    jim.fd(30)
    jim.rt(90)
    jim.circle(50)

  #arm 1
  def arm_1(self,jim):
    jim.seth(160)
    jim.fd(Drawings.arm_length/2)
    jim.rt(20)
    jim.fd(Drawings.arm_length/2)

  #arm 2
  def arm_2(self,jim):
    jim.seth(20)
    jim.fd(Drawings.arm_length/2)
    jim.lt(20)
    jim.fd(Drawings.arm_length/2)

  #leg 1
  def leg_1(self,jim):
    jim.seth(270)
    jim.fd(150)
    jim.seth(230)

  #leg 2
  def leg_2(self,jim):
    jim.seth(270)
    jim.fd(150)
    jim.seth(310)
"""
class word_works(object):

  def generate_word():
    words = {
      1 : "community",
      2 : "volcano",
      3 : "sunrise",
      4 : "hypothesis",
      5 : "information",
      6 : "sample",
      7 : "probability",
      8 : "Brazil",
      9 : "railroad",
      10 : "diamond",
      11 : "question",
      12 : "agreement",
      13 : "reflection",
      14 : "elephant",
      15 : "pigeon",
      16 : "technology",
      17 : "multiply",
      18 : "appetite",
      19 : "designer",
      20 : "function",
      21 : "pandemic",
      22 : "interface",
      23 : "helicopter",
      24 : "algorithm",
      25 : "orange"
    }
    word_key = random.randint(1, 25)
    selected_word = words[word_key]
    return selected_word

  def display_word(self,selected_word):
    word = selected_word.generate_word()
    length_of_word = len(word)
    display_letterinword = "_"*(length_of_word)
    print(display_letterinword)


number_of_guesses = 0
correct_guesses = 0
incorrect_guesses = 0
guesses = []

def repeated_letter(x,y):
  if x in y:
    print("\nThis letter has already been guessed!")
    print("List of guessed letters:", guesses,"\n")
  else:
    pass

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs
  

while number_of_guesses < length_of_word:
  guess = input("\nEnter a letter to guess: ")
  
  repeated_letter(guess, guesses)
  
  if guess not in word:
    incorrect_guesses+=1
    
  while guess in word:
  
    position = list_duplicates_of(word,guess)
    print(position)
    counter= 0
    
    for i in position:
      #
      index = position[counter]
      #turn the string into a list
      display_letterinword = list(display_letterinword)

      #you can only insert a new item into a certain index if it's a list
      display_letterinword.insert(index, guess)
      display_letterinword.pop(index+1)
    
      #turn the list back into a string
      display_letterinword = ''.join(display_letterinword)
      correct_guesses += 1
      
      counter+=1
    print (display_letterinword)
    number_of_guesses +=1
    break
    
  if correct_guesses == length_of_word:
    print("You guessed correctly!")
    break
  if incorrect_guesses == 7:
    print("You reached the guessing limit")
    break
  
    #problem: same letter in two different positions, how do we make sure both go in? --- solved

  







  
 
