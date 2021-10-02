#
from tkinter import *

class tmr_def_window(Tk):
	def __init__(self,type):
		super().__init__()
		if type==1:
			s1,s2=NORMAL,DISABLED
			self.config(bg="#dfff4f")
		elif type==2:
			s2,s1=NORMAL,DISABLED
			self.config(bg="#a9765d")
		self.title("Tennis match referee")
		self.iconbitmap("C:/Users/hp/OneDrive/Desktop/TennisMatchReffree/ico/tennis-racket.ico")
		self.minsize(1080,780)
		#widgets
		st_menu=Menu(self)
		outmatch_menu=Menu(st_menu,tearoff=0)
		inmatch_menu=Menu(st_menu,tearoff=0)
		outmatch_menu.add_command(label="New tennis match")
		outmatch_menu.add_command(label="Load tennis match")
		outmatch_menu.add_separator()
		inmatch_menu.add_command(label="Edit")
		inmatch_menu.add_command(label="Save")
		inmatch_menu.add_command(label="Save as...")
		inmatch_menu.add_separator()
		inmatch_menu.add_command(label="Exit")
		outmatch_menu.add_command(label="Exit")
		st_menu.add_cascade(label="Out Match",menu=outmatch_menu,state=s1)
		st_menu.add_cascade(label="In Match",menu=inmatch_menu,state=s2)
		self.config(menu=st_menu)
