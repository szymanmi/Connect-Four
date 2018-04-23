from tkinter import *
from functools import partial


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()

		self.label_info = Label(self, height=1).grid()
		self.label_score = Label(self.label_info, text='Wynik 0:0').grid(row=0, column=0, columnspan=2)
		self.label_turn = Label(self.label_info, text='Tura gracza X').grid(row=0, column=2, columnspan=2)
		self.button_reset = Button(self.label_info, text='reset').grid(row=0, column=4, columnspan=2)

		self.label_buttons = Label(self).grid()
		self.img = PhotoImage(file="a.png")
		self.bttn = []
		for i in range(7):
			self.bttn.append(Button(self.label_buttons))
			self.bttn[i].config(image=self.img, command=partial(self.new_move, i))
			self.bttn[i].grid(row=1, column=i)

		self.label_fields = Label(self).grid()
		self.img2 = PhotoImage(file="b.png")
		self.label_field = []

		for i in range(6):
			tmp = []
			for j in range(7):
				tmp.append(Label(self.label_fields))
				tmp[j].config(image=self.img2)
				tmp[j].grid(row=i+2, column=j)
			self.label_field.append(tmp)

		self.red = PhotoImage(file='red.png')

	def new_move(self, n):
		self.label_field[5][n].config(image=self.red)


root = Tk()
root.title('projekcik')
root.geometry('420x490')
app = Application(root)
root.mainloop()
