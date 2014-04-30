#!/usr/bin/python

import csv
import sys

listed = dict()

def memoize(f):
	return lambda *args: listed[args] if args in listed else listed.update({args: f(*args)}) or listed[args]

@memoize
def fib(n):
	a,b = 0,1
	while a<n:
		yield a
		a,b = b, a+b

fibonacci = []

def listCount(array):
	count = 0
	for i in array:
		count+=1
	return count

def listFib():
	sort = sorted(listed.items(), key=lambda x: x[1])
	for i,j in sort:
		fibonacci.append(j)
	listCount(fibonacci)

def findMods(modNum, array):
	for i in range(2, modNum):
		for j in fibonacci:
			array.append((i, (j, j % i)))

def findLength(array1, array2):
	array2.append((0, 'N/A'))
	array2.append((1, 1))
	tempArrays = []
	for i in array1:
		tempArray = []
		for count in range(listCount(array1)-1):
			if i[0] == array1[count][0]:
				tempArray.append(array1[count])
		if tempArray not in tempArrays:
			tempArrays.append(tempArray)
	for arrayCount in range(listCount(tempArrays)):
		temporary = []
		tempArray = tempArrays.pop(0)
		temporary.append(tempArray.pop(0))
		for count in range(listCount(tempArray)):
			if tempArray[0][1][1] != 0:
				temporary.append(tempArray.pop(0))
			elif (tempArray[0][1][1] == 0) and (tempArray[1][1][1] != 1):
				temporary.append(tempArray.pop(0))
			else:
				array2.append((tempArray[0][0], listCount(temporary)))
				break

moded = []
numLength = []

def sanityCheck(count, modNum):
	if (modNum-1) == 7 and count <= 16:
		return None, 'Not enough information.', 'Please increase the count of fibonacci numbers', 'or decrease the length count number.'
	else: return (True, 0, 0)

def main(count=0, modNum=0):
	fib(count)
	listFib()
	findMods(modNum, moded)
	findLength(moded, numLength)
	# print moded
	with open('PisanoPeriods.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Modulus Number', 'Series Length'])
		writer.writerow(['0', 'Division by Zero Error'])
		writer.writerows(numLength[1:])
	print numLength

if __name__ == '__main__':
	count, modNum = int(sys.argv[1]), (int(sys.argv[2])+1)
	checks = sanityCheck(count, modNum)
	if checks[0] == True:
		main(count, modNum)
	else:
		print checks[1]
		print checks[2]
		print checks[3]