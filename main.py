from tkinter import *
from functools import partial


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()

		self.img = PhotoImage(file="a.png")
		self.red = PhotoImage(file='red.png')
		self.yellow = PhotoImage(file='yellow.png')

		self.values = [[0 for i in range(7)] for j in range(6)]
		self.turn = 1

		self.label_info = Label(self, height=1).grid()
		self.label_score = Label(self.label_info, text='Wynik 0:0')
		self.label_score.grid(row=0, column=0, columnspan=2)
		self.label_turn = Label(self.label_info, text='Tura gracza X')
		self.label_turn.grid(row=0, column=2, columnspan=2)
		self.button_reset = Button(self.label_info, text='reset', command=self.reset)
		self.button_reset.grid(row=0, column=4, columnspan=2)

		self.label_buttons = Label(self).grid()
		self.bttn = []
		for col in range(7):
			self.bttn.append(Button(self.label_buttons))
			self.bttn[col].config(image=self.red, command=partial(self.new_move, col))
			self.bttn[col].grid(row=1, column=col)

		self.label_fields = Label(self).grid()
		self.img2 = PhotoImage(file="b.png")
		self.label_field = []

		for i in range(6):
			tmp = []
			for j in range(7):
				tmp.append(Label(self.label_fields))
				tmp[j].config(image=self.img2)
				tmp[j].grid(row=i + 2, column=j)
			self.label_field.append(tmp)

	def new_move(self, col):
		if self.legal_move(col):
			self.update_fields(col, self.calculate_row(col))

	def legal_move(self, col):
		# if field in zero row and clicked column is not used yet then this column is not full -> move is legal
		if self.values[0][col] is 0:
			return True
		return False

	def calculate_row(self, col):
		for row in range(5, -1, -1):
			if self.values[row][col] is 0:
				return row

	def update_fields(self, col, row):
		self.values[row][col] = 1
		if self.turn == 1:
			self.label_field[row][col].config(image=self.red)
			for i in range(7):
				self.bttn[i].config(image=self.yellow)
			self.turn = 2
		else:
			self.label_field[row][col].config(image=self.yellow)
			for i in range(7):
				self.bttn[i].config(image=self.red)
			self.turn = 1

		self.label_turn.config(text='Tura gracza ' + str(self.turn))

	def reset(self):
		for i in range(6):
			for j in range(7):
				self.values[i][j] = 0
				self.label_field[i][j].config(image=self.img2)


root = Tk()
root.title('projekcik')
root.geometry('420x490')
app = Application(root)
root.mainloop()
