import turtle
import random 

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
    11 : "query",
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

    
 
