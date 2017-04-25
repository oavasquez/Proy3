from Tkinter import *

class App(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master, bg="#009688")
		self.master.title("IA: Proy No. 3")
		self.ancho_pantalla = self.winfo_screenwidth()
		self.alto_pantalla = self.winfo_screenheight()
