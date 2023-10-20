#what ?? : it is a package: it is importing : loading
#Why ??: because some packages are in different python files
#How?? : with syntax "import"
import random as bat
import getpass as gp
while (1):
  #List the choices like rock , paper and scissors

  GameList = ["Rock", "Paper", "Scissor"]
  #you have to like make coiches that can be picked and say if they won or not.
  Vihaans_pick = gp.getpass(
      prompt=
      '\nVihaan,Please select rock,paper or scissors\n Enter Exit if you get bored\n'
  ).upper()  # u can type any rock, Rock, RoCk.etc...
  #Virat gets to pick
  virats_pick = gp.getpass(
      prompt=  #getpass is a pass to use the thing
      '\nvirat,Please select rock,paper or scissor\n Enter Exit if you get bored\n'
  ).upper()

  if (Vihaans_pick == "Exit".upper()):
    print("Game Over")
    break  #for this it is if i pick exit then the game is over and we take a break and it will display game over
  print(Vihaans_pick, virats_pick)

  if (Vihaans_pick == virats_pick):
    print("Tie")  #this is if me and virat pick the same thing it will say tie
  elif (
      Vihaans_pick == "Rock".upper()
  ):  #we made upper because then even if you type rock in lowercase it will auto =maticly make it uppercase.
    if (virats_pick == "Scissor".upper()):
      print("Vihaan wins!!!Hurray!!!!Yay!!!")
    if (virats_pick == "Paper".upper()): 
      print("virat wins"):
  elif (Vihaans_pick == "Paper".upper()):
    if (virats_pick == "Scissor".upper()):
      print("virat wins!!!!")
    if (virats_pick == "Rock".upper()):
      print("Vihaan wins!!Excellent!!")

  elif (Vihaans_pick == "Scissor".upper()):
    if (virats_pick == "Rock".upper()):
      print("virat wins!"):
    if (virats_pick == "Paper"):
      print("Vihaan!!The winner!!")
  print("\nStart new round")  #and this is to start a new round
