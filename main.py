import random
import os

class DynamicGrid:

	# initialize with randomly generated numbers already made
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
		pass
	def find_element(self, element):
		numList = []
		i = 0
		for row in self.matrix:
			j = 0
			for column in row:
				if element == column:
					print(f"{i+1},{j+1}")
					arr = [i, j]
					numList.append(arr)
				j += 1
			i += 1
		if not numList:
			print ("Element not Found")
		
	def view_matrix(self):
		for row in self.matrix:
			print(row)

def main():
	matrix = DynamicGrid()
	print("Dynamic Matrix Generated!")

	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Welcome to a two-dimentional matrix processor" \
		"1. View the matrix" \
		"2. Total sum of the matrix" \
		"3. Smallest number in the matrix" \
		"4. Largest number in the matrix" \
		"5. Sort a row" \
		"6. Search for an element" \
		"7. Exit" \
		"")

		choice = input("Enter a choice (1 - 7): ")
		if (choice == "1"):
			matrix.view_matrix()
		elif (choice == "2"):
			print(f"Total Sum: {matrix.total_sum()}")
		elif (choice == "3"):
			matrix.find_smallest()
		elif (choice == "4"):
			matrix.find_


if __name__ == "__main__":
	main()
