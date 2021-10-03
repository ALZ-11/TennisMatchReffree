#
from tkinter import *
import time

class piw(Tk):	#piw: players' information window
	def __init__(self):
		super().__init__()
		self.title("Tennis match referee")
		self.iconbitmap("C:/Users/hp/OneDrive/Desktop/TennisMatchReffree/ico/tennis-racket.ico")
		self.config(bg="#dfff4f")
		self.minsize(1080,780)
		#window titles and subtitles
		title=Label(self,text="Welcome to: Tennis match referee",font=("Algerian",40,"bold"),fg="#6f4fff",bg="#dfff4f",pady=10)
		subtitle1=Label(self,text="by Adam LOZI",font=("Times New Roman",20,"italic"),fg="#6f4fff",bg="#dfff4f")
		subtitle2=Label(self,text="Input match information:",font=("",30,"bold underline"),fg="#6f4fff",bg="#dfff4f",pady=35)
		remark=Label(self,text="(Do not worry about the capitalization of the letters)",font=("",20,"bold"),fg="#6f4fff",bg="#dfff4f")
		#window frames
		frame=Frame(self,bg='#dfff4f',pady=20)
		#players' info labels	
		widget1,widget2,widget3,widget4,widget5=Label(frame,text="Player one's full name:",font=("Bahnschrift",20),bg="#dfff4f",pady=10),Label(frame,text="Player two's full name:",font=("Bahnschrift",20),bg="#dfff4f",pady=10),Label(frame,text="Number of sets in the match:",font=("Bahnschrift",20),bg="#dfff4f",pady=10),Label(frame,text="Number of games per set:",font=("Bahnschrift",20),bg="#dfff4f",pady=10),Label(frame,text="First serve to player no:",font=("Bahnschrift",20),bg="#dfff4f",pady=10)
		invalid=Label(self,bg="#dfff4f",font=("",15,"bold"),fg="#FE3434",pady=20)
		#players' entrys
		i1,i2,i3,i4,i5=StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
		input1,input2,input3,input4,input5=Entry(frame,textvariable=i1,bd=3,relief=SUNKEN),Entry(frame,textvariable=i2,bd=3,relief=SUNKEN),Entry(frame,textvariable=i3,bd=3,relief=SUNKEN),Entry(frame,textvariable=i4,bd=3,relief=SUNKEN),Entry(frame,textvariable=i5,bd=3,relief=SUNKEN)
		#boutons de la fenetre
		match_button=Button(self,text="Let the match commence!",font=("",15,"bold"),bd=10, relief=RIDGE)
		#display
		title.pack()
		subtitle1.pack()
		subtitle2.pack()
		remark.pack()

		widget1.grid(row=0,column=0)
		widget2.grid(row=1,column=0)
		widget3.grid(row=2,column=0)
		widget4.grid(row=3,column=0)
		widget5.grid(row=4,column=0)
		input1.grid(row=0,column=1)
		input2.grid(row=1,column=1)
		input3.grid(row=2,column=1)
		input4.grid(row=3,column=1)
		input5.grid(row=4,column=1)

		frame.pack()
		invalid.pack()
		match_button.pack()


class tennis_main(Tk):
	def __init__(self):
		super().__init__()
		#customized window layout
		self.title("Tennis match referee")
		self.iconbitmap("C:/Users/hp/OneDrive/Desktop/TennisMatchReffree/ico/tennis-racket.ico")
		self.minsize(1080,780)
		self.config(bg="#dfff4f")
		#window menus
			#commands
			#menus
		main_menu=Menu(self)
				#sub menus
					#outmatch
		outmatch_menu=Menu(main_menu,tearoff=0)

		outmatch_menu.add_command(label="New match")
		outmatch_menu.add_command(label="Load match")
		outmatch_menu.add_separator()
		outmatch_menu.add_command(label="Exit")
					#inmatch
		inmatch_menu=Menu(main_menu,tearoff=0)

		inmatch_menu.add_command(label="Edit")
		inmatch_menu.add_command(label="Save")
		inmatch_menu.add_command(label="Save as...")
		inmatch_menu.add_separator()
		inmatch_menu.add_command(label="Exit")
					#settings
		settings_menu=Menu(main_menu,tearoff=0)

		settings_menu.add_command(label="Language")
		settings_menu.add_command(label="Theme")
					#about
		about_menu=Menu(main_menu,tearoff=0)

		about_menu.add_command(label="App")
		about_menu.add_command(label="Author")
			#add sub menus and configuration
		main_menu.add_cascade(label="Out Match",menu=outmatch_menu)
		main_menu.add_cascade(label="In Match",menu=inmatch_menu,state=DISABLED)
		main_menu.add_cascade(label="Settings",menu=settings_menu)
		main_menu.add_cascade(label="About",menu=about_menu)

		self.config(menu=main_menu)


a=piw()
a.mainloop()