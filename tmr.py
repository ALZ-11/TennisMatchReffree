#

from tkinter import *
from ex_mods.tmr_class import *

def lbcg():
	s1sbl.config(text=str(tm.gstat()[4]))
	g1sbl.config(text=str(tm.gstat()[2]))
	p1sbl.config(text=str(p(tm.gstat()[0])))
	s2sbl.config(text=str(tm.gstat()[5]))
	g2sbl.config(text=str(tm.gstat()[3]))
	p2sbl.config(text=str(p(tm.gstat()[1])))
	if tm.gstat()[6]==1:
		sl.grid(row=1,column=0)
	else:
		sl.grid(row=1,column=1)
	if tm.gstat()[2]==tm.gstat()[3]==tm.nog:
		if tm.gstat()[0]==0 and tm.gstat()[1]==0:
			if tm.gstat()[6]==1:
				tsl.grid(row=2,column=0)
			else:
				tsl.grid(row=2,column=1)
		elif tm.tgstat()[2]==1:
			tsl.grid(row=2,column=0)
		else:
			tsl.grid(row=2,column=1)
	else:
		tsl.grid_forget()


def p1pt():
	reffree_statement_label.config(text=tm.point1())
	lbcg()
	if tm.gstat()[4]==tm.nos//2+1:
		player1_button.config(state=DISABLED)
		player2_button.config(state=DISABLED)

def p2pt():
	reffree_statement_label.config(text=tm.point2())
	lbcg()
	if tm.gstat()[5]==tm.nos//2+1:
		player1_button.config(state=DISABLED)
		player2_button.config(state=DISABLED)


def ltmc():
	global tm
	global reffree_statement_label
	global s1sbl,g1sbl,p1sbl,s2sbl,g2sbl,p2sbl,sl,tsl
	global player1_button,player2_button
	if len(i1.get())==0 or len(i2.get())==0:
		invalid.config(text="Invalid name for player 1 or player 2")
	elif i3.get().isnumeric()==False or i4.get().isnumeric()==False:
		invalid.config(text="Invalid number of sets or games per set")
	elif float(i3.get())==0 or float(i4.get())==0:
		invalid.config(text="There should be at least 1 set and 1 game in the match")
	elif i5.get().isnumeric()==False or (float(i5.get())!=1 and float(i5.get())!=2):
		invalid.config(text="Invalid first serve, pick between 1 or 2")
	else:
		tm=tennismatch(i1.get(),i2.get(),int(i3.get()),int(i4.get()),int(i5.get()))
		#fenetre match
		match_button.config(state=DISABLED,text="Close the current match to start a new one")
		mw=Toplevel(piw)	#mw: match window
		mw.title("Tennis match referee")
		mw.iconbitmap("ico/tennis-racket.ico")
		mw.config(bg="#a9765d")
		mw.minsize(1080,780)
		#titres de la fenetre
		title2=Label(mw,text=f"{lastname(i1.get())} Vs {lastname(i2.get())}",font=("Algerian",50,"bold"),fg="#5d90a9",bg="#a9765d")
		#boites de la fenetre
		score_board=Frame(mw,bg='#a9765d', pady=50)
		players_buttons=Frame(mw,bg='#a9765d')
		#widgets texte de la fenetre
		label1=Label(mw,text="Who scored?",font=("",30),bg="#a9765d",pady=30)
		players_score_board_label=Label(score_board,text="Players",fg="#5d90a9",bg="#a9765d",font=("",20,"bold underline"))
		sets_score_board_label=Label(score_board,text="Sets",fg="#5d90a9",bg="#a9765d",font=("",20,"bold underline"))
		games_score_board_label=Label(score_board,text="Games",fg="#5d90a9",bg="#a9765d",font=("",20,"bold underline"))
		points_score_board_label=Label(score_board,text="Points",fg="#5d90a9",bg="#a9765d",font=("",20,"bold underline"))
		player1_label=Label(score_board,text=lastname(i1.get()).title(),fg="#FFFFFF",bg="#a9765d",font=("",20,"bold"))
		s1sbl,g1sbl,p1sbl,s2sbl,g2sbl,p2sbl=Label(score_board,text="0",fg="#FFFFFF",bg="#a9765d",font=("",20,"bold")),Label(score_board,text="0",fg="#FFFFFF",bg="#a9765d",font=("",20,"bold")),Label(score_board,text="0",fg="#FFFFFF",bg="#a9765d",font=("",20,"bold")),Label(score_board,text="0",fg="#FFFFFF",bg="#a9765d",font=("",20,"bold")),Label(score_board,text="0",fg="#FFFFFF",bg="#a9765d",font=("",20,"bold")),Label(score_board,text="0",fg="#FFFFFF",bg="#a9765d",font=("",20,"bold"))
		player2_label=Label(score_board,text=lastname(i2.get()).title(),fg="#FFFFFF",bg="#a9765d",font=("",20,"bold"))
		sl=Label(players_buttons,text="(Server)",font=("",30,"bold"),fg="#36ff72",bg="#a9765d")
		tsl=Label(players_buttons,text="(Tie server)",font=("",20,"bold"),fg="#FFA500",bg="#a9765d")
		label2=Label(mw,text="Referee statement:",font=("",30),bg="#a9765d",pady=30)
		reffree_statement_label=Label(mw,text="",font=("",30,"bold"),fg="#5d90a9",bg="#a9765d")
		#boutons de la fenetre
		player1_button=Button(players_buttons,text=lastname(i1.get()).title(),font=("Magneto",30,"bold"))
		player2_button=Button(players_buttons,text=lastname(i2.get()).title(),font=("Magneto",30,"bold"))
		player1_button.config(command=p1pt,bd=10, relief=SUNKEN)
		player2_button.config(command=p2pt,bd=10, relief=SUNKEN)
		#protocoles de la fenetre
		def mw_closed():
			mw.destroy()
			match_button.config(state=NORMAL,text="Let the match commence!")
		mw.protocol("WM_DELETE_WINDOW", mw_closed)
		#affichage
		title2.pack()
		players_score_board_label.grid(row=0,column=0,padx=30)
		sets_score_board_label.grid(row=0,column=1,padx=30)
		games_score_board_label.grid(row=0,column=2,padx=30)
		points_score_board_label.grid(row=0,column=3,padx=30)
		player1_label.grid(row=1,column=0)
		s1sbl.grid(row=1,column=1)
		g1sbl.grid(row=1,column=2)
		p1sbl.grid(row=1,column=3)
		player2_label.grid(row=2,column=0)
		s2sbl.grid(row=2,column=1)
		g2sbl.grid(row=2,column=2)
		p2sbl.grid(row=2,column=3)
		score_board.pack()
		label1.pack()
		player1_button.grid(row=0,column=0,padx=20)
		player2_button.grid(row=0,column=1,padx=20)
		if int(i5.get())==1:
			sl.grid(row=1,column=0)
		else:
			sl.grid(row=1,column=1)
		players_buttons.pack()
		label2.pack()
		reffree_statement_label.pack()
		mw.mainloop()
	
def playinfowin():
	global piw
	global i1,i2,i3,i4,i5
	global match_button,invalid
	#fenetre infos de joueurs
	piw = Tk()	#piw: players' information window
	piw.title("Tennis match referee")
	piw.iconbitmap("ico/tennis-racket.ico")
	piw.config(bg="#dfff4f")
	piw.minsize(1080,780)
	#titres de la fenetre
	title=Label(piw,text="Welcome to: Tennis match referee",font=("Algerian",40,"bold"),fg="#6f4fff",bg="#dfff4f",pady=10).pack()
	subtitle1=Label(piw,text="by Adam LOZI",font=("Times New Roman",20,"italic"),fg="#6f4fff",bg="#dfff4f").pack()
	subtitle2=Label(piw,text="Input match information:",font=("",30,"bold underline"),fg="#6f4fff",bg="#dfff4f",pady=35).pack()
	#boites de la fenetre
	frame=Frame(piw,bg='#dfff4f',pady=20)
	#widgets texte de la fenetre
	remark=Label(piw,text="(Do not worry about the capitalization of the letters)",font=("",20,"bold"),fg="#6f4fff",bg="#dfff4f").pack()
	widget1=Label(frame,text="Player one's full name:",font=("Bahnschrift",20),bg="#dfff4f",pady=10).grid(row=0,column=0)
	widget2=Label(frame,text="Player two's full name:",font=("Bahnschrift",20),bg="#dfff4f",pady=10).grid(row=1,column=0)
	widget3=Label(frame,text="Number of sets in the match:",font=("Bahnschrift",20),bg="#dfff4f",pady=10).grid(row=2,column=0)
	widget4=Label(frame,text="Number of games per set:",font=("Bahnschrift",20),bg="#dfff4f",pady=10).grid(row=3,column=0)
	widget5=Label(frame,text="First serve to player no:",font=("Bahnschrift",20),bg="#dfff4f",pady=10).grid(row=4,column=0)
	invalid=Label(piw,bg="#dfff4f",font=("",15,"bold"),fg="#FE3434",pady=20)
	#entrees de la fenetre
	i1,i2,i3,i4,i5=StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
	input1=Entry(frame,textvariable=i1,bd=3,relief=SUNKEN).grid(row=0,column=1)
	input2=Entry(frame,textvariable=i2,bd=3,relief=SUNKEN).grid(row=1,column=1)
	input3=Entry(frame,textvariable=i3,bd=3,relief=SUNKEN).grid(row=2,column=1)
	input4=Entry(frame,textvariable=i4,bd=3,relief=SUNKEN).grid(row=3,column=1)
	input5=Entry(frame,textvariable=i5,bd=3,relief=SUNKEN).grid(row=4,column=1)
	#boutons de la fenetre
	match_button=Button(piw,text="Let the match commence!",font=("Magneto",15,"bold"),command=ltmc,bd=10, relief=RIDGE)
	#affichage
	frame.pack()
	invalid.pack()
	match_button.pack()
	piw.mainloop()
playinfowin()