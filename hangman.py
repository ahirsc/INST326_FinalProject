import random
import turtle
print("Let's play hangman!\n")

#Turtle
t = turtle.Turtle()
t.ht()
t.lt(180)
t.pensize(2)
t.penup()
t.rt(-90)
t.fd(150)
t.rt(90)
t.bk(-50)
t.pendown()
t.pencolor("black")
    
def draw_post():
  #drawing of the base of the post
  t.bk(100)
  t.fd(200)

  #drawing of the post
  t.bk(100)
  t.rt(90)
  t.fd(280) #height of the post
  t.lt(-90)
  t.fd(140)
  t.lt(-90)
  t.fd(50)
  
def draw_head():
  #head
  t.dot(50)

def draw_body():
  #body
  t.fd(130)
  t.lt(-180)
  t.fd(80)

def draw_leftArm():
  #Left arm
  t.rt(-100)
  t.fd(65)
  t.lt(180)
  t.fd(65)

def draw_rightArm():
  #right arm
  t.rt(20)
  t.fd(65)
  t.lt(-180)
  t.fd(65)
  #move
  t.penup()
  t.rt(-100)
  t.pendown()

def draw_leftLeg():  
  #leg1
  t.fd(85)
  t.lt(-35)
  t.fd(65)
  t.lt(-180)
  t.fd(65)

def draw_rightLeg():  
  #leg2
  t.lt(-110)
  t.fd(65)

def generate_word():
  words = {
    1: "community",
    2: "volcano",
    3: "sunrise",
    4: "hypothesis",
    5: "information",
    6: "sample",
    7: "probability",
    8: "Brazil",
    9: "railroad",
    10: "diamond",
    11: "question",
    12: "answer",
    13: "reflection",
    14: "elephant",
    15: "pigeon",
    16: "technology",
    17: "multiply",
    18: "appetite",
    19: "designer",
    20: "function",
    21: "pandemic",
    22: "interface",
    23: "helicopter",
    24: "algorithm",
    25: "orange"
  }
  word_key = random.randint(1, 25)
  selected_word = words[word_key]
  return selected_word


word = generate_word()
length_of_word = len(word)
display_letterinword = "_" * (length_of_word)
print(display_letterinword)
number_of_guesses = 0
correct_guesses = 0
incorrect_guesses = 0
guesses = []
dummy_list = []
draw_post()


def repeated_letter(x, y):
  if x in y:
    print("\nThis letter has already been guessed!")
    print("List of guessed letters:", guesses, "\n")
  else:
    pass


def list_duplicates_of(seq, item):
  start_at = -1
  locs = []
  while True:
    try:
      loc = seq.index(item, start_at + 1)
    except ValueError:
      break
    else:
      locs.append(loc)
      start_at = loc
  return locs


while number_of_guesses < length_of_word:
  try:
    guess = str(input("\nEnter a letter to guess: "))
  except:
    print("Only letters please")
  if len(guess) != 1:
    print("Only one letter at a time please")

  repeated_letter(guess, guesses)
  if guess in guesses:
    dummy_list.append(guess)
  else:
    guesses.append(guess)

    
  if guess not in word:
    incorrect_guesses += 1
    print(incorrect_guesses)
    if incorrect_guesses == 1:
      draw_head()
    elif incorrect_guesses == 2:
      draw_body()
    elif incorrect_guesses == 3:
      draw_leftArm()
    elif incorrect_guesses == 4:
      draw_rightArm()
    elif incorrect_guesses == 5:
      draw_leftLeg()
    elif incorrect_guesses == 6:
      draw_rightLeg()

  while guess in word:

    position = list_duplicates_of(word, guess)
    print(position)
    counter = 0

    for i in position:
      #
      index = position[counter]
      #turn the string into a list
      display_letterinword = list(display_letterinword)

      #you can only insert a new item into a certain index if it's a list
      display_letterinword.insert(index, guess)
      display_letterinword.pop(index + 1)

      #turn the list back into a string
      display_letterinword = ''.join(display_letterinword)
      correct_guesses += 1

      counter += 1
    print(display_letterinword)
    number_of_guesses += 1
    break
    
  if correct_guesses == length_of_word:
    print("You guessed correctly! You win!!!!")
    break
    
  if incorrect_guesses == 6:
    print("You reached the guessing limit")
    print("The word was: ", word)
    break
  

