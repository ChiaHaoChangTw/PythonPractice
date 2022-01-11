import random

class Player():
	#symbol is x or o
	def __init__(self, symbol):
		self.letter = symbol
	def getMove(self, game):
		pass

class HumanPlayer(Player):
	def __init__(self, symbol):
		super().__init__(symbol)
	def getMove(self, game):
		validIdx = False
		idx = None
		while not validIdx:
			in = input(self.symbol + "\'s turn. Please enter move (0 ~ 9): ")
			try: 
				idx = int(in)
				if idx not in game.emptyIndex():
					raise ValueError
				validIdx = true
			except ValueError:
				print("Please enter valid move. Try again.")
		return idx 

class ComputerPlayer(Player):
	def __init__(self, symbol):
		super().__init__(symbol)
	def getMove(self, game):
		return random.choice(game.emptyIndex())
