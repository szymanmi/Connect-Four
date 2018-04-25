class GameRules:
	def __init__(self):
		self.flag = 0
		self.values = [[0 for i in range(7)] for j in range(6)]

	# this method determines whether current move can be executed (column is not full)
	def legal_move(self, col):
		# if field in zero row and clicked column is not used yet then this column is not full -> move is legal
		if self.values[0][col] is 0:
			return True
		return False

	# this method is calculating the correct row in which coin should be placed depending on picked column
	def calculate_row(self, col, turn):
		for row in range(5, -1, -1):
			if self.values[row][col] is 0:
				self.values[row][col] = turn
				return row

	def reset(self):
		for i in range(6):
			for j in range(7):
				self.values[i][j] = 0

	def get_values(self):
		return self.values


class ConnectFourRules(GameRules):
	def check_end(self):
		for row in range(6):
			for first_column in range(4):
				if self.values[row][first_column] is self.values[row][first_column + 1] is self.values[row][
					first_column + 2] is self.values[row][first_column + 3] and self.values[row][first_column] is not 0:
					return True

		for col in range(7):
			for row in range(3):
				if self.values[row][col] is self.values[row + 1][col] is self.values[row + 2][col] is \
						self.values[row + 3][col] and self.values[row][col] is not 0:
					return True

		for row in range(3):
			for col in range(4):
				if self.values[row][col] is self.values[row + 1][col + 1] is self.values[row + 2][col + 2] is \
						self.values[row + 3][col + 3] and self.values[row][col] is not 0:
					return True

		for col in range(3, 7):
			for row in range(3):
				if self.values[row][col] is self.values[row + 1][col - 1] is self.values[row + 2][col - 2] is \
						self.values[row + 3][col - 3] and self.values[row][col] is not 0:
					return True
		return False
