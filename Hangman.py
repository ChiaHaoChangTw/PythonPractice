import random
from WordsForHangman import words
import string

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

if __name__ == "__main__":
	playHangman()
