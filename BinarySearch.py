import random
import time

def linearSearch(list, target):
	for i in range(len(list)):
		if list[i] == target:
			return i
	return -1

def binarySearch(list, target):
	l = 0
	r = len(list) - 1
	while l <= r:
		mid = l + (r - l) // 2
		if list[mid] == target:
			return mid
		elif target < list[mid]:
			r = mid - 1
		else:
			l = mid + 1
	return -1

if __name__ == "__main__":

	#make random list
	sortedList = []
	size = 10000
	while len(sortedList) < size:
		sortedList.append(random.randint(-size, size))
	sortedList = sorted(sortedList)

	#linear search
	start = time.time()
	for target in sortedList:
		linearSearch(sortedList, target)
	end = time.time()
	print("Linear search time: ", (end - start), " seconds.")

	#binary search
	start = time.time()
	for target in sortedList:
		binarySearch(sortedList, target)
	end = time.time()
	print("Binary search time: ", (end - start), " seconds.")