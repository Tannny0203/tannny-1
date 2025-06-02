from turtle import Turtle,Screen
import random 

is_on = False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which one will win the race? Enter color:")
color =["red","orange","blue","black","green","beige","purple"]
y_positions =[-60,-40,-20,10,30,50,70]
print(user_bet)
all_turtles =[]




for turtle_index in range(0,7):
  new_turtle=Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.color(color[turtle_index])
  new_turtle.goto(x=-240,y=y_positions[turtle_index])
  
  all_turtles.append(new_turtle)


if user_bet:
  is_on=True

while is_on:

  for turtle in all_turtles:
    rand_distance = random.randint(0,10)
    new_turtle.forward(rand_distance)
  
  
screen.exitonclick()

