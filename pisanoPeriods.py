#!/usr/bin/env python

def fib(n):
	a,b,c = 0,1,0
	while c<n:
		yield a
		c+=1
		a,b = b, a+b

def lenCount(array):
	count = 0
	for i in array:
		count+=1
	return count

def findMods(fibList, num):
	tempList = []
	for i in range(2, num):
		tempModList = []
		for item in fibList:
			tempModList.append(int(int(item) % i))
		tempList.append([i, tempModList])
	return tempList

def listCount(list, findList, initialIndex = 1):
	periodIndex = list.index(findList[0], initialIndex)
	if int(periodIndex):
		if list[periodIndex+1] == findList[1] and list[periodIndex+2] == findList[2]:
			return int(2), int(periodIndex)
		else:
			return listCount(list, findList, periodIndex+1)
	else:
		return 1	

def remod(fibList, num, fibLen):
	fibLen += 10
	tempFibList = []
	for item in fib(fibLen):
		tempFibList.append(item)
	fibList = tempFibList
	print(len(fibList))
	tempList = []
	for i in fibList:
		tempList.append(int(int(i) % num))
	print(tempList)
	return tempList

def findLength(array1, array2):
	array2.append((0, 'N/A'))
	array2.append((1, 1))
	tempArrays = []
	for i in array1:
		tempArray = []
		for count in range(lenCount(array1)-1):
			if i[0] == array1[count][0]:
				tempArray.append(array1[count])
		if tempArray not in tempArrays:
			tempArrays.append(tempArray)
	for arrayCount in range(lenCount(tempArrays)):
		temporary = []
		tempArray = tempArrays.pop(0)
		temporary.append(tempArray.pop(0))
		for count in range(lenCount(tempArray)):
			if tempArray[0][1][1] != 0:
				temporary.append(tempArray.pop(0))
			elif (tempArray[0][1][1] == 0) and (tempArray[1][1][1] != 1):
				temporary.append(tempArray.pop(0))
			else:
				array2.append((tempArray[0][0], lenCount(temporary)))
				break

def findLength2(modedList, fibList, fibLen):
	periodList = []
	for entry in modedList:
		# initialize the periodIndex var so that we can use it after the while
		periodIndex = 0
		# find the second instance of [0, 1, 1] in the list inside each entry
		while True:
			# make sure that the list is long enough to get the entire period
			# periodIndex is the length of our period
			count, periodIndex = listCount(entry[1], [0, 1, 1])
			if count > 1: # count should only ever be 1 or 2
				break
			print(entry)
			# since its not long enough, make it longer
			fibLen += 10
			entry[1] = remod(fibList, entry[0], fibLen)
		periodList.append([entry[0], periodIndex])
	return periodList

def writeToFile(infile, array):
	import csv
	with open (infile, 'wb') as csvfile:
		file = csv.writer(csvfile)
		file.writerow(['Modulus Number', 'Series Length'])
		file.writerow(['0', 'Division by Zero Error'])
		file.writerow(['1', '1'])
		file.writerows(array[1:])
	print('Done')

def main(modNum=0):
	count = 100
	moded, numLength, fibonacci = [], [], []
	# Get the fibonacci sequence
	for num in fib(count):
		fibonacci.append(num)
	# Find the modulus numbers for each in fib
	moded = findMods(fibonacci, modNum)
	# Find the length of the pisano periods
	# for each modulus number
	numLength = findLength2(moded, fibonacci, count)
	print(numLength)
	#writeToFile('PisanoPeriods.csv', numLength) # under development

if __name__ == '__main__':
	import sys
	modNum = int(sys.argv[1])+1
	main(modNum)