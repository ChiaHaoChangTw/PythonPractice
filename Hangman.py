import random
from WordsForHangman import words
import string
from HangmanVisual import livesVisualDict

def printWords(words):
	print(words)

def getWord(words):
	word = random.choice(words)
	while "-" in word or " " in word:
		word = random.choice(words)
	return word.lower()

def playHangman():
	word = getWord(words)
	wordChars = set(word)
	allChars = set(string.ascii_lowercase)
	guessedChars = set()
	lives = 7
	while len(wordChars) > 0 and lives > 0:
		print("You have ", lives, " lives left, and you have used these characters: ", " ".join(guessedChars))
		result = set()
		for wordChar in word:
			if wordChar in guessedChars:
				result.add(wordChar)
			else:
				result.add("_")
		print(livesVisualDict[lives])
		print("Current result: ", " ".join(result))
		guess = input("Guess a letter: ").lower()
		if guess in allChars - guessedChars:
			guessedChars.add(guess)
			if guess in wordChars:
				wordChars.remove(guess)
				print(guess, " is a correct guess.")
			else:
				--lives
				print(guess, " is an incorrect guess.")
		elif guess in guessedChars:
			print("You have already guessed this letter. Please guess another one.")
		else:
			print("Not a valid letter. Please guess a valid letter again.")
	if lives == 0:
		print(livesVisualDict[lives])
		print("You died. The correct word is ", word)
	else:
		print("Congratulations! You successfully guessed the word ", word, ".")

if __name__ == "__main__":
	playHangman()
