import random
import re

class Board:
	def init(self, boardSize, numMine):
		self.boardSize = boardSize
		self.numMine = numMine
		self.board = self.makeBoard()
		self.initBoardValue()
		self.dicovered = set()
	
	def makeBoard(self):
		board = [[None for i in range(self.boardSize)] for j in range(self.boardSize)]
		currMine = 0
		while currMine < numMine
			locIndex = random.randint(0, self.boardSize ** 2 - 1);
			row = locIndex // self.boardSize
			col = locIndex % self.boardSize
			if board[row][col] == "*":
				continue
			board[rol][col] = "*"
			currMine += 1
		return board
	
	def initBoardValue(self):
		for i in range(self.boardSize)
			for j in range(self.boardSize)
				if self.board[i][j] == "*":
					continue
				self.board[i][j] = self.numNeighborMine(i, j)
	
	def numNeighborMine(self, row, col):
		num = 0
		for i in range(max(0, row - 1), min(self.boardSize - 1, row + 1) + 1):
			for j in range(max(0, col - 1), min(self.boardSize - 1, col + 1) + 1):
				if i == row and j = col:
					continue
				if self.board[i][j] == "*":
					num += 1
		return num
	
	def discover(self, row, col):
		pass
	
	def toString(self):
		pass

def playGame():
	pass

if __name__ == "__main__":
	playGame()
	







