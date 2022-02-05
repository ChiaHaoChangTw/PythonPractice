def forLoop():
	#loop a collection
	users = {'chang': 'active', 'chia': 'inactive', 'hao': 'active'}
	activeUsers = {}
	for user, status in users.items():
		if status == 'active':
			activeUsers[user] = status
	for status in activeUsers.values():
		print(status, end = ',')
	print('\n')
	
	#loop a sequence
	list = ['a','b','c','d']
	for i in range(len(list)):
		print(i, list[i], end = ',')
	print('\n')

	#for-else loop
	for n in range(2, 10):
		for x in range(2, n):
			if n % x == 0:
				print(n, 'equals', x, '*', n // x)
				break
		else:
			print(n, 'is a prime number')	
	print()

	#enumerate
	for i, v in enumerate(['tic', 'tac', 'toe']):
		print(i, v)
	print()

#* and ** before function arguments
def shop(kind, *arguments, **keywords):
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)
	for arg in arguments:
        	print(arg)
	print("-" * 40)
	for kw in keywords:
		print(kw, ":", keywords)

if __name__ == "__main__":
	forLoop()
	shop("Limburger","It's very runny, sir.", "It's really very, VERY runny, sir.",
		shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")
