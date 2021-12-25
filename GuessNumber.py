import random

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

if __name__ == "__main__":
	guessNumber(30)
