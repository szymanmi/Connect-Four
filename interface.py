from tkinter import *
import tkinter.messagebox
from functools import partial
import logic


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()

		self.game_logic = logic.ConnectFourRules()

		self.img = PhotoImage(file="b.png")
		self.img_player = [PhotoImage(file='red.png'), PhotoImage(file='yellow.png')]

		modes = ['Connect ' + str(i) for i in range(3, 6)]								### LC

		# first main label contains: current score, turn info, reset button
		self.label_1 = Label(self, height=1).grid()
		self.label_score = Label(self.label_1, text='Wynik\n0:0')
		self.label_score.grid(row=0, column=0, columnspan=1)
		self.label_turn = Label(self.label_1, text='Tura\ngracza\n 1')
		self.label_turn.grid(row=0, column=1, columnspan=1)
		self.button_reset = Button(self.label_1, text='reset', command=lambda: self.reset())		### LAMBDA
		self.button_reset.grid(row=0, column=2, columnspan=1)
		self.game_mode = StringVar(self.label_1)
		self.game_mode.set(modes[1])
		self.w = OptionMenu(self.label_1, self.game_mode, *modes)
		self.w.grid(row=0, column=3, columnspan=2)
		self.button_apply = Button(self.label_1, text='zmień tryb', command=lambda: self.change_mode())		### LAMBDA
		self.button_apply.grid(row=0, column=5, columnspan=2)

		# second main label contains 7 clickable buttons
		self.label_2 = Label(self).grid()
		self.bttn = [Button(self.label_2) for i in range(7)]										### LC
		###
		self.bttn[0].config(image=self.img_player[0], command=lambda: self.new_move(0))				### LAMBDA
		self.bttn[0].grid(row=1, column=0)
		for col in range(1,7):
			self.bttn[col].config(image=self.img_player[0], command=partial(self.new_move, col))
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
	def new_move(self, clicked_col):
		# if move cannot be performed then do nothing
		if self.game_logic.column_not_full(clicked_col):
			self.update_fields(clicked_col, self.game_logic.calculate_row(clicked_col))
		else:
			tkinter.messagebox.showinfo(":(", "Nie zmieści się już :/")

	# this method is called when user picked correct column to put coin in
	def update_fields(self, col, row):
		self.game_logic.update_fields(row, col)
		self.label_field[row][col].config(image=self.img_player[self.game_logic.get_turn()])

		if self.game_logic.draw():
			tkinter.messagebox.showinfo("koniec", "remis")
			self.reset()

		elif not self.game_logic.check_end():
			self.game_logic.change_turn()
			for i in range(7):
				self.bttn[i].config(image=self.img_player[self.game_logic.get_turn()])
			self.label_turn.config(text='Tura\ngracza\n' + str(self.game_logic.get_turn() + 1))

		else:
			tkinter.messagebox.showinfo("koniec", "wygrał gracz " + str(self.game_logic.get_turn() + 1))
			self.game_logic.add_point()
			temp = self.game_logic.get_score()
			self.label_score.config(text='Wynik\n' + str(temp[0]) + ':' + str(temp[1]))

			self.reset()

	def reset(self):
		self.game_logic.reset()
		self.label_turn.config(text='Tura\ngracza\n' + str(self.game_logic.get_turn() + 1))

		for i in range(7):
			self.bttn[i].config(image=self.img_player[0])
		for i in range(6):
			for j in range(7):
				self.label_field[i][j].config(image=self.img)

	def change_mode(self):
		self.label_score.config(text='Wynik\n0:0')
		new_mode = str(self.game_mode.get())
		if new_mode == 'Connect 5':
			self.game_logic = logic.ConnectFiveRules()
		elif new_mode == 'Connect 4':
			self.game_logic = logic.ConnectFourRules()
		elif new_mode == 'Connect 3':
			self.game_logic = logic.ConnectThreeRules()
		self.reset()
