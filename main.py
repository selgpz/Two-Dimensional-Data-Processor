import random

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
		smallest = 101
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


	def quicksort(self, array):
		less = []
		equal = []
		greater = []

		if len(array) > 1:
			pivot = array[0]
			for x in array:
				if x < pivot:
					less.append(x)
				elif x == pivot:
					equal.append(x)
				elif x > pivot:
					greater.append(x)
			return self.quicksort(less) + equal + self.quicksort(greater)
		else:
			return array

	def sort_row(self, row):
		array = self.matrix.pop(row)
		self.matrix.insert(row, self.quicksort(array))

	def find_element(self, element):
		numList = []
		i = 0
		for row in self.matrix:
			j = 0
			for column in row:
				if element == column:
					print(f"({i+1}, {j+1})")
					arr = [i, j]
					numList.append(arr)
				j += 1
			i += 1

		if not numList:
			return True
		else:
			return False

	def view_matrix(self):
		print("")
		i = 0
		for row in self.matrix:
			i += 1
			print(f"{i}. {row}")

"""
Main function below!
"""
def main():
	matrix = DynamicGrid()
	print("Dynamic Matrix Generated!")

	while True:
		print("" \
		"Welcome to a two-dimentional matrix processor\n" \
		"1. View the matrix\n" \
		"2. Total sum of the matrix\n" \
		"3. Smallest number in the matrix\n" \
		"4. Largest number in the matrix\n" \
		"5. Sort a row\n" \
		"6. Search for an element\n" \
		"7. Exit\n" \
		"")

		choice = input("Enter a choice (1 - 7): ")
		if (choice == "1"):
			matrix.view_matrix()
			print("")

		elif (choice == "2"):
			print(f"Total Sum: {matrix.total_sum()}")

		elif (choice == "3"):
			num = matrix.find_smallest()
			print("" \
			f"Smallest number is {num}" \
			"")
			if matrix.find_element(num):
				print("There is no smallest number.")

		elif (choice == "4"):
			num = matrix.find_biggest()
			print("" \
			f"Biggest number is {num}" \
			"")
			if matrix.find_element(num):
				print("There is no biggest number.")

		elif (choice == "5"):

			string = input("Enter a row to sort (1 - 10): ")
			if not string.isdecimal:
				print("Invalid input. Please enter a number.")
				continue

			row = int(string)
			matrix.sort_row(row - 1)
		elif (choice == "6"):

			string = input("Enter an element: ")
			if not string.isdecimal:
				print("Invalid input. Please enter a number.")
				continue

			element = int(string)
			matrix.find_element(element)
		elif (choice == "7"):
			print("Exiting...")
			break
		else:
			print("Invalid choice! Please try again!")

if __name__ == "__main__":
	main()
