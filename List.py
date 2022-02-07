def listOperations():
	fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
	print(fruits.count('apple'))
	print(fruits.count('tangerine'))
	print(fruits.index('banana'))
	print(fruits.index('banana', 4))
	fruits.reverse()
	print(fruits)
	fruits.append('grape')
	print(fruits)
	fruits.sort()
	print(fruits)
	print(fruits.pop())

	#used as stack
	stk = [3,4,5]
	stk.append(6)
	stk.append(7)
	print(stk)
	print(stk.pop())
	print(stk)
	stk.pop()
	stk.pop()
	print(stk)

	#list comprehensions
	squares = [x**2 for x in range(10)]
	print(squares)
	newList = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
	print(newList)
	matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
	revMatrix = [[row[i] for row in matrix] for i in range(4)]
	print(revMatrix)

if __name__ == '__main__':
	listOperations()
