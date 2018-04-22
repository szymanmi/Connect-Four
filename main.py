from tkinter import *


class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.bttn_clicks = 0
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.bttn1 = Button(self, text='Liczba klikniec: 0', command=self.update_count)
		self.bttn1.grid()

	def update_count(self):
		self.bttn_clicks += 1
		self.bttn1['text'] = 'Liczba klikniec: ' + str(self.bttn_clicks)


root = Tk()
root.title('projekcik')
root.geometry('640x480')
app = Application(root)
root.mainloop()
