from tkinter import *


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()

		self.img = PhotoImage(file="a.png")
		self.label = Label(root)
		self.label.grid()
		self.bttn = []
		for i in range(6):
			self.bttn.append(Button(self.label))
			self.bttn[i].config(image=self.img)
			self.bttn[i].grid(row=0, column=i)


root = Tk()
root.title('projekcik')
root.geometry('640x480')
app = Application(root)
root.mainloop()
