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



grid = DynamicGrid()
print(grid.total_sum())
