#First iteration of RPS program against an automated opponent. A random integer from zero to 2 is chosen 
#representing rock, paper, or scissors. The player is prompted to make their selection,
#then boolean logic is followed to determine who wins.
import random

comp = random.randint(0, 2)
print("rock...")
print("paper...")
print("scissors...")
print("SHOOT!")
print("Please enter name for Player 1: ")
p1_name = input()
while p1_name == "":
	print("No name detected. Please enter your name, or a fake one (give me something to work with here xD): ")
	p1_name = input()

p1 = input(p1_name + ", please make your move. Choose 'rock', 'paper', or 'scissors': \n")
#For Computer random play
#0 = rock
#1 = paper
#2 = scissors

#If computer chooses rock
if comp == 0:
	if p1 == "rock":
		print("The computer also chose rock.")
		print("It's a tie!")
	elif p1 == "paper":
		print("The computer chose rock.")
		print("Paper covers rock; " + p1_name + " wins!")
	elif p1 == "scissors":
		print("The computer chose rock.")
		print("Rock crushes scissors; Better luck next time!")
	elif p1 == "":
		print("You didn't make a choice! Please play again and choose one of the 3 options.")
	else:
		print("- Something went wrong; Maybe check spelling or don't capitalize your choices?")
#If computer chooses paper
elif comp == 1:
	if p1 == "paper":
		print("The computer also chose paper.")
		print("It's a tie!")
	elif p1 == "rock":
		print("The computer chose paper.")
		print("Paper covers rock; Better luck next time!")
	elif p1 == "scissors":
		print("The computer chose paper.")
		print("Scissors cuts paper; " + p1_name + " wins!")
	elif p1 == "":
		print("You didn't make a choice! Please play again and choose one of the 3 options.")
	else:
		print("- Something went wrong; Maybe check spelling or don't capitalize your choices?")
#If computer chooses scissors
elif comp == 2:
	if p1 == "scissors":
		print("The computer also chose scissors.")
		print("It's a tie!")
	elif p1 == "rock":
		print("The computer chose scissors.")
		print("Rock crushes scissors; " + p1_name + " wins!")
	elif p1 == "paper":
		print("The computer chose scissors.")
		print("Scissors cuts paper; Better luck next time!")
	elif p1 == "":
		print("You didn't make a choice! Please play again and choose one of the 3 options.")
	else:
		print("- Something went wrong; Maybe check spelling or don't capitalize your choices?")

#elif p1 == "":
#	print("No text detected. Please re-run the program and enter 'rock', 'paper' or 'scissors' when prompted.")
#Acccounting for typos or other wildcards
else:
	print("yeet")
 	#print("- Something went wrong; Maybe check spelling or don't capitalize your choices?")
