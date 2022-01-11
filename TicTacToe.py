import math
from TicTacToePlayer import HumanPlayer, ComputerPlayer

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

	def makeMove(self, index, player):
		if self.board[index] == " ":
			self.board[index] = player
			if self.isWin(index, player):
				self.winner = player
			return True
		return False

	def isWin(self, index, player):
		rowIdx = math.floor(index / 3)
		currRow = self.board[rowIdx * 3 : (rowIdx + 1) * 3]
		if all([i == player for i in currRow]):
			return True
		colIdx = index % 3
		currCol = [self.board[colIdx + i * 3] for i in range(3)]
		if all([i == player for i in currCol]):
                        return True
		if index % 2 == 0:
			diagonal1 = [self.board[i] for i in [0, 4, 8]]
			if all([i == player for i in diagonal1]):
                        	return True
			diagonal2 = [self.board[i] for i in [2, 4, 6]]
			if all([i == player for i in diagonal2]):
                        	return True
		return False

	def emptyIndex(self):
		return [i for i, index in enumerate(self.board) if index == " "]
	
	def hasEmptyIndex(self):
		return " " in self.board

	def numEmptyIndex(self):
		return self.board.count(" ")

def play(game, xPlayer, oPlayer, printGame = True):
	if printGame:
		game.printBoardIndex()
	player = "x"
	while game.hasEmptyIndex():
		pass