import random

def play():
	human = input("Please enter your choice: 'rock', 'paper', or 'scissors'\n")
	computer = random.choice(["rock", "paper", "scissors"])
	if human == computer:
		print("Tie!")
		return
	if humanWin(human, computer):
		print("You won!")
		return 
	print("You lost!")
	return

def humanWin(human, computer):
	if (human == "rock" and computer == "scissors" or human == "scissors" and computer == "paper" or human == "paper" and computer == "rock"):
		return True
	return False

if __name__ == '__main__':
	play()