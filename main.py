from tkinter import *
import tkinter.messagebox
from functools import partial
import logic


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()

		self.logic = logic.GameRules()

		self.img = PhotoImage(file="b.png")
		self.red = PhotoImage(file='red.png')
		self.yellow = PhotoImage(file='yellow.png')

		modes = ['Connect 3', 'Connect 4', 'Connect 5']

		self.values = [[0 for i in range(7)] for j in range(6)]
		self.turn = 1

		# first main label contains: current score, turn info, reset button
		self.label_1 = Label(self, height=1).grid()
		self.label_score = Label(self.label_1, text='Wynik 0:0')
		self.label_score.grid(row=0, column=0, columnspan=2)
		self.label_turn = Label(self.label_1, text='Tura gracza 1')
		self.label_turn.grid(row=0, column=2, columnspan=2)
		self.button_reset = Button(self.label_1, text='reset', command=self.reset)
		self.button_reset.grid(row=0, column=4, columnspan=1)

		self.game_mode = StringVar(self.label_1)
		self.game_mode.set(modes[1])
		self.w = OptionMenu(self.label_1, self.game_mode, *modes)

		self.w.grid(row=0, column=5, columnspan=2)
		# second main label contains 7 clickable buttons
		self.label_2 = Label(self).grid()
		self.bttn = []
		for col in range(7):
			self.bttn.append(Button(self.label_2))
			self.bttn[col].config(image=self.red, command=partial(self.new_move, col))
			self.bttn[col].grid(row=1, column=col)

		# third main label contains 6x7 labels representing fields for coins in game
		self.label_3 = Label(self).grid()
		self.label_field = []
		# creating 6x7 labels
		for i in range(6):
			tmp = []
			for j in range(7):
				tmp.append(Label(self.label_3))
				tmp[j].config(image=self.img)
				tmp[j].grid(row=i + 2, column=j)
			self.label_field.append(tmp)

	# this method is called whenever user clicked on any of 7 buttons
	def new_move(self, col):
		# if move cannot be performed then do nothing
		if self.logic.legal_move(self.values, col):
			self.update_fields(col, self.calculate_row(col))
		else:
			tkinter.messagebox.showinfo(":(", "no tu już się nie zmieści typie")

	# this method is calculating the correct row in which coin should be placed depending on picked column
	def calculate_row(self, col):
		for row in range(5, -1, -1):
			if self.values[row][col] is 0:
				return row

	# this method is called when user picked correct column to put coin in
	def update_fields(self, col, row):
		# updating list
		self.values[row][col] = self.turn
		if self.turn == 1:
			self.label_field[row][col].config(image=self.red)
			for i in range(7):
				self.bttn[i].config(image=self.yellow)
		else:
			self.label_field[row][col].config(image=self.yellow)
			for i in range(7):
				self.bttn[i].config(image=self.red)
		if not self.check_end():
			self.change_turn()
			self.label_turn.config(text='Tura gracza ' + str(self.turn))

	def reset(self):
		self.turn = 1
		self.label_turn.config(text='Tura gracza ' + str(self.turn))
		for i in range(7):
			self.bttn[i].config(image=self.red)
		for i in range(6):
			for j in range(7):
				self.values[i][j] = 0
				self.label_field[i][j].config(image=self.img)

	def check_end(self):
		if logic.ConnectFourRules.check_end(self.values):
			tkinter.messagebox.showinfo("koniec", "wygrał gracz " + str(self.turn))
			self.reset()
			return True
		return False

	def change_turn(self):
		if self.turn is 1:
			self.turn = 2
		else:
			self.turn = 1


root = Tk()
root.title('projekcik')
root.geometry('420x490')
app = Application(root)
root.mainloop()
