class Player():
	#symbol is x or o
	def __init__(self, symbol):
		self.letter = symbol
	def move(self, game):
		pass

class HumanPlayer(Player):
	def __init__(self, symbol):
		super().__init__(symbol)
	def move(self, game):
		pass

class ComputerPlayer(Player):
	def __init__(self, symbol):
		super().__init__(symbol)
	def move(self, game):
		pass
