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
		total_sum = 0
		for row in self.matrix:
			for i in row:
				total_sum += i
			return total_sum

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

	def sort_row(self):
	def find_element(self, element):
	def view_matrix(seelf):

def main():
	matrix = DynamicGrid()
	print("Dynamic Matrix Generated!")

	while True:
		print("Welcome to a two-dimentional matrix processor" \
		"1. View the matrix" \
		"2. Total sum of the matrix" \
		"3. Smallest number in the matrix" \
		"4. Largest number in the matrix" \
		"5. Sort a row" \
		"6. Search for an element" \
		"7. Exit" \
		"")

		choice = input("Enter a choice (1 - 7):")
		if (choice == "1"):
			matrix.print
		else if (choice == "2"):

if __name__ == "__main__":
	main()
