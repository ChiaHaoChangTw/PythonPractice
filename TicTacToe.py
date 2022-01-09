class TicTacToe():
	def __init__(self):
		self.board = self.makeBoard()
		self.winner = None

	@staticmethod
	def makeBoard():
		return [" " for i in range(9)]

	def printBoard(self):
		for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
			print("|", " | ".join(row), "|")

	@staticmethod
	def printBoardIndex():
		boardIndex = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
		for rowIndex in boardIndex:
			print("|", " | ".join(rowIndex), "|")

	def emptyIndex():
		return [i for i, index in enumerate(self.board) if index == " "]
