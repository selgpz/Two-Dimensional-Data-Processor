import random

class DynamicGrid:
	#
	def __init__(self):
		self.matrix = []
		for i in range(10):
			row = []
			for i in range(10):
				row.append(random.randint(1, 100))
			self.matrix.append(row)

	def total_sum(self):
		# loop on the
		sum = 0
		for row in self.matrix:
			for i in row:
				sum = sum + i
			return sum
		
	def find_smallest(self):
		smallest = 100
		
		for row in self.matrix:
			for i in row:
				if i < smallest:
					smallest = i
				
		return smallest
	def find_biggest(self):
		biggest = 0
		for row in self.matrix:
			for i in row:
				if i > biggest:
					biggest = i
		return biggest

	def find_element(self, element):
		numList = []
		i = 0
		for row in self.matrix:
			j = 0
			for column in row:
				if element == column:
					print(f"{i+1},{j+1}")
					arr = [i,j]
					numList.append(arr)		
				j += 1
			i += 1
		if not numList:
			print ("Element not Found")	
		

grid = DynamicGrid()

print(grid.matrix)
element = 100
grid.find_element(element)
#print(grid.find_smallest())
#print(grid.find_biggest())
