# Author Vihaan and Akshata
import random as bat
import getpass as gp
while (1):
  #List the choices like rock , paper and scissors

  GameList = ["Rock", "Paper", "Scissor"]
  #you have to like make coiches that can be picked and say if they won or not.
  Player1_pick = gp.getpass(
      prompt=
      '\nPlayer1,Please select rock,paper or scissors\n Enter Exit if you get bored\n'
  ).upper()  # u can type any rock, Rock, RoCk.etc...
  #Player2 gets to pick
  Player2s_pick = gp.getpass(
      prompt=  #getpass is a pass to use the thing
      '\nPlayer2,Please select rock,paper or scissor\n Enter Exit if you get bored\n'
  ).upper()

  if (Player1s_pick == "Exit".upper()):
    print("Game Over")
    break  #for this it is if i pick exit then the game is over and we take a break and it will display game over
  print(Player1s_pick, Player2s_pick)

  if (Player1s_pick == Player2s_pick):
    print("Tie")  #this is if me and Player2 pick the same thing it will say tie
  elif (
      Player1s_pick == "Rock".upper()
  ):  #we made upper because then even if you type rock in lowercase it will auto =maticly make it uppercase.
    if (Player2s_pick == "Scissor".upper()):
      print("Player1 wins!!!Hurray!!!!Yay!!!")
    if (Player2s_pick == "Paper".upper()): 
      print("Player2 wins"):
  elif (Player1s_pick == "Paper".upper()):
    if (Player2s_pick == "Scissor".upper()):
      print("Player2 wins!!!!")
    if (Player2s_pick == "Rock".upper()):
      print("Player1 wins!!Excellent!!")

  elif (Player1s_pick == "Scissor".upper()):
    if (Player2s_pick == "Rock".upper()):
      print("Player2 wins!"):
    if (Player2s_pick == "Paper"):
      print("Player1!!The winner!!")
  print("\nStart new round")  #and this is to start a new round
