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



grid = DynamicGrid()

print(grid.matrix)

print(grid.find_smallest())
