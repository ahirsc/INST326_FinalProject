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
  """
  Functionality: Draw the base of the post for the hangman
  """

  #drawing of the base of the post
  t.bk(100)
  t.fd(200)

  #drawing of the post
  t.bk(100)
  t.rt(90)
  t.fd(280)  #height of the post
  t.lt(-90)
  t.fd(140)
  t.lt(-90)
  t.fd(50)


def draw_head():
  """
  Function to draw the head of the hangman
  """
  t.dot(50)


def draw_body():
  """
  Function to draw the body of the hangman
  """
  t.fd(130)
  t.lt(-180)
  t.fd(80)


def draw_leftArm():
  """
  Function to draw the left arm of the hangman
  """
  t.rt(-100)
  t.fd(65)
  t.lt(180)
  t.fd(65)


def draw_rightArm():
  """
  Function to draw the right arm of the hangman
  """
  t.rt(20)
  t.fd(65)
  t.lt(-180)
  t.fd(65)
  #move
  t.penup()
  t.rt(-100)
  t.pendown()


def draw_leftLeg():
  """
  Function to draw the left leg of the hangman
  """
  t.fd(85)
  t.lt(-35)
  t.fd(65)
  t.lt(-180)
  t.fd(65)


def draw_rightLeg():
  """
  Function to draw the right leg of the hangman
  """
  t.lt(-110)
  t.fd(65)


class Word_Generator:
  """
  Class to generate a word to be used in the game.
  Returns the selected word
  Methods: 
  __init__: creates a word dictionary assigning keys to words
  generate_word: randomly picks an integer from 1 to 25 and pulls that key from the dictionary
  """

  def __init__(self):
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
    self.words = words

  def generate_word(self):
    word_key = random.randint(1, 25)
    self.selected_word = self.words[word_key]
    return self.selected_word

def repeated_letter(x, y):
  """
  Function to store the guesses already made by the user
  Parameters:
  x: the letter tht will be guessed by the user
  y: the word generated by the word generator function
  Invoked when user tries to guess the same letter more than once.
  """
  if x in y:
    print("\nThis letter has already been guessed!")
    print("List of guessed letters:", guesses, "\n")
  else:
    pass


def list_duplicates_of(seq, item):
  """
  Functionality: Identify the duplicate letters in the generated word.
  Parameters: 
  seq (str): the word to be guessed
  item (str): the letter input by the user
  Returtns:
  locs(list): List of all the indexes where that letter is located in the string
  """
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

#Create an instance of the word generator class
game = Word_Generator()
word = game.generate_word()

length_of_word = len(word)
display_letterinword = "_" * (length_of_word)
print(display_letterinword)
number_of_guesses = 0
correct_guesses = 0
incorrect_guesses = 0
guesses = []
dummy_list = []
draw_post()
  
if __name__ == "__main__":
  """
  Main functionalities of the program.
  """
  
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
