import random
from WordsForHangman import words
import string
from HangmanVisual import livesVisualDict

def printWords(words):
	print(words)

def getWord(words):
	word = random.choice(words)
	while "-" in word or " " in word":
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
		result = []
		for wordChar in word:
			if wordChar in gussedChars:
				result.add(wordChar)
			else:
				result.add("_")
		print(livesVisualDict[lives])
		print("Current result: ", " ".join(result))

if __name__ == "__main__":
	playHangman()
