
# NOTE: Requires a space optimization to only use A[S of cardinality M] * 2 space
# 		Run in 64-bit python to prevent Memory Error at 2GB
import time
import math
import itertools


##########
# IMPLEMENTATION 1
##########
numCities = 0
cities = {}		# Contains cities[1] -> cities[numCities]

class City:
	x = 0
	y = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getDistanceTo(self, i2):
		return math.sqrt(math.pow(self.x - cities[i2].x, 2) + math.pow(self.y - cities[i2].y, 2))

def readGraph(filename):
	global cities
	global numCities

	file = open(filename, "r")
	isline1 = True
	cityIndex = 1
	for line in file:
		if isline1:
			numCities = int(line)
			isline1 = False
			continue
		cities[cityIndex] = City(float(line.split(" ")[0]), float(line.split(" ")[1]))
		cityIndex += 1

def tsp():
	vertices = cities.keys()
	A = {}

	# Do this here, as m starts from 2
	A[tuple([1])] = {}
	A[tuple([1])][1] = 0

	for m in range(2, numCities + 1):	# m = subproblem size (cardinality of S)
		print("M =", m)
		combos = itertools.combinations(vertices, m)

		if m >= 4:
			toDel = itertools.combinations(vertices, m - 2)
			for key in toDel:
				if 1 in key:
					del A[key]

		for S in combos:			# Take all possible subsets of size m
			# POSSIBLE OPTIMIZATION HERE:
				# Map all possible subsets as bitmap strings and just set cities which are included in the subset to 1.
				# This would reduce memory consumption a lot and speed up the loop operations.
				# E.G: 0000000000000000000000111 (single string) as a dictionary key instead of the tuple of n integers.
			if 1 not in S:			# S has to contain 1
				continue
			# Set up base cases for this m
			A[S] = {}
			A[S][1] = float("inf")

			for j in S:				# Iterate through all j in S where j != 1 (j = 1 has been taken care of in base cases)
				if j == 1:
					continue
				minASj = float("inf")
				for k in S:			# Iterate through all k in S where k != j and find best k for the subproblem
					if k == j:
						continue
					sNew = list(S)
					sNew.remove(j)
					if A[tuple(sNew)][k] + cities[k].getDistanceTo(j) < minASj:
						minASj = A[tuple(sNew)][k] + cities[k].getDistanceTo(j)
				A[S][j] = minASj

	# Find the shortest tour out of all narrowed candidates
	minTour = float("inf")
	for j in range(2, numCities + 1):
		if A[tuple(range(1, numCities + 1))][j] + cities[j].getDistanceTo(1) < minTour:	# Just compare the total distances including the final hop
			print(tuple(range(1, numCities + 1)))
			minTour = A[tuple(range(1, numCities + 1))][j] + cities[j].getDistanceTo(1)

	return minTour

###########
# END IMPLEMENTATION 1
###########

###########
# IMPLEMENTATION 2
###########
