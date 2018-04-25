class ConnectFourRules:
	@staticmethod
	def check_end(x):
		for row in range(6):
			for first_column in range(4):
				if x[row][first_column] is x[row][first_column + 1] is x[row][
					first_column + 2] is x[row][first_column + 3] and x[row][first_column] is not 0:
					return True

		for col in range(7):
			for row in range(3):
				if x[row][col] is x[row + 1][col] is x[row + 2][col] is \
						x[row + 3][col] and x[row][col] is not 0:
					return True

		for row in range(3):
			for col in range(4):
				if x[row][col] is x[row + 1][col + 1] is x[row + 2][col + 2] is \
						x[row + 3][col + 3] and x[row][col] is not 0:
					return True

		for col in range(3, 7):
			for row in range(3):
				if x[row][col] is x[row + 1][col - 1] is x[row + 2][col - 2] is \
						x[row + 3][col - 3] and x[row][col] is not 0:
					return True
		return False

