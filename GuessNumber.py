import random

#human guess
def guessNumber(upperLimit):
	theNumber = random.randint(1, upperLimit)
	guess = 0
	while guess != theNumber:
		guess = int(input(f"Guess a number between 1 and {upperLimit}: "))
		if guess < theNumber:
			print("Guess a higher number.")
		elif guess > theNumber:
			print("Guess a lower number.")
	print(f"Congratulations! You have guessed the number {theNumber} correctly.")

#computer guess
def computerGuess(upperLimit):
	lowerBound = 1
	upperBound = upperLimit
	result = ""
	while result != "C":
		guess = random.randint(lowerBound, upperBound)
		result = input(f"Is {guess} too high (H), too low (L), or correct (C)?")
		if result == "H":
			upperBound = guess - 1
		elif result == "L":
			lowerBound = guess + 1
	print(f"Computer has guessed your number, {guess}, correctly.")

if __name__ == "__main__":
	playWithComputer = input(f"Would you like to play with computer? (Y/N): ")
	upperLimit = int(input(f"Please type in an integer number to decide your upper limit: "))
	if playWithComputer == "Y":
		computerGuess(upperLimit)
	else:
		guessNumber(upperLimit)
