#-*- coding: utf-8 -*-

import timeit
from random import randint
from random import shuffle

def insertionSort(list):
	for x in range(1, len(list)):
		key = list[x]
		i = x-1
		while(i >= 0 and list[i] > key):
			list[i+1] = list[i]
			i -= 1
		list[i+1] = key
	return list

def createBigRandList():
	randNum = randint(100, 1000) # the size of the list to be sorted 
	randList = []

	for x in range(0, randNum):
		randList.append(x)

	shuffle(randList)
	return randList

def printResults(list, func):
	print("The result of sorting the random list: " + str(func(list)))

# time test
def insertionSortTimeTest():
	SETUP_CODE = '''
from __main__ import insertionSort
from __main__ import createBigRandList
from __main__ import printResults
from random import randint
from random import shuffle
	'''
	TEST_CODE = '''
bigRandList = createBigRandList()
printResults(bigRandList, insertionSort)
	'''
	# if one wants to test it for more inputs then change the repeat/or number variable 
	times = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 1, number = 1)

	print('Time it took to sort the list: {}'.format(min(times)))


if __name__ == "__main__": 
	# testing for small inputs
	smallTestList = [1,2,3,4,5]
	smallTestList2 = [2,1,4,5,3]
	smallTestList3 = [5,4,3,2,1]

	printResults(smallTestList, insertionSort)
	printResults(smallTestList2, insertionSort)
	printResults(smallTestList3, insertionSort)

	# lets try with some bigger ones and test the speed via the timeit module 
	insertionSortTimeTest()