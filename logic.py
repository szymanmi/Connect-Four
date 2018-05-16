class ConnectFourRules:
	def __init__(self):
		self.values = [[-1 for i in range(7)] for j in range(6)]		### LC
		self.turn = 0
		self.score = [0, 0]

	# this method determines whether current move can be executed (column is not full)
	def column_not_full(self, clicked_col):
		# if field in zero row and clicked column is not used yet then this column is not full -> move is legal
		if self.values[0][clicked_col] is -1:
			return True
		return False

	# this method is calculating the correct row in which coin should be placed depending on picked column
	def calculate_row(self, col):
		for row in range(5, -1, -1):
			if self.values[row][col] is -1:
				return row

	def draw(self):
		for i in range(6):
			for j in range(7):
				if self.values[i][j] == -1:
					return False
		return True

	def update_fields(self, row, col):
		self.values[row][col] = self.turn

	def reset(self):
		self.turn = 0
		for i in range(6):
			for j in range(7):
				self.values[i][j] = -1

	def get_values(self):
		return self.values

	def change_turn(self):
		if self.turn == 0:
			self.turn = 1
		else:
			self.turn = 0

	def get_turn(self):
		return self.turn

	def get_score(self):
		return self.score

	def add_point(self):
		self.score[self.turn] += 1

	def check_end(self):
		for row in range(6):
			for first_column in range(4):
				if self.values[row][first_column] is self.values[row][first_column + 1] is self.values[row][
					first_column + 2] is self.values[row][first_column + 3] and self.values[row][
					first_column] is not -1:
					return True

		for col in range(7):
			for row in range(3):
				if self.values[row][col] is self.values[row + 1][col] is self.values[row + 2][col] is \
						self.values[row + 3][col] and self.values[row][col] is not -1:
					return True

		for row in range(3):
			for col in range(4):
				if self.values[row][col] is self.values[row + 1][col + 1] is self.values[row + 2][col + 2] is \
						self.values[row + 3][col + 3] and self.values[row][col] is not -1:
					return True

		for col in range(3, 7):
			for row in range(3):
				if self.values[row][col] is self.values[row + 1][col - 1] is self.values[row + 2][col - 2] is \
						self.values[row + 3][col - 3] and self.values[row][col] is not -1:
					return True
		return False


class ConnectFiveRules(ConnectFourRules):
	def check_end(self):
		for row in range(6):
			for col in range(3):
				if self.values[row][col] is self.values[row][col + 1] is self.values[row][col + 2] is self.values[row][
					col + 3] is self.values[row][col + 4] and self.values[row][col] is not -1:
					return True

		for col in range(7):
			for row in range(2):
				if self.values[row][col] is self.values[row + 1][col] is self.values[row + 2][col] is \
						self.values[row + 3][col] is self.values[row + 4][col] and self.values[row][col] is not -1:
					return True

		for col in range(3):
			for row in range(2):
				if self.values[row][col] is self.values[row + 1][col + 1] is self.values[row + 2][col + 2] is \
						self.values[row + 3][col + 3] is self.values[row + 4][col + 4] and self.values[row][
					col] is not -1:
					return True

		for col in range(4, 7):
			for row in range(2):
				if self.values[row][col] is self.values[row + 1][col - 1] is self.values[row + 2][col - 2] is \
						self.values[row + 3][col - 3] is self.values[row + 3][col - 3] is self.values[row + 4][
					col - 4] and self.values[row][col] is not -1:
					return True
		return False


class ConnectThreeRules(ConnectFourRules):
	def check_end(self):
		for row in range(6):
			for col in range(5):
				if self.values[row][col] is self.values[row][col + 1] is self.values[row][col + 2] and self.values[row][
					col] is not -1:
					return True

		for row in range(4):
			for col in range(7):
				if self.values[row][col] is self.values[row + 1][col] is self.values[row + 2][col] and self.values[row][
					col] is not -1:
					return True

		for row in range(4):
			for col in range(5):
				if self.values[row][col] is self.values[row + 1][col + 1] is self.values[row + 2][col + 2] and \
						self.values[row][col] is not -1:
					return True

		for col in range(2, 7):
			for row in range(4):
				if self.values[row][col] is self.values[row + 1][col - 1] is self.values[row + 2][col - 2] and \
						self.values[row][col] is not -1:
					return True

		return False
