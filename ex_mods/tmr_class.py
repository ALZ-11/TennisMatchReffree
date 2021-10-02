#
from .st_mods.st_funcs import *

class tennismatch():
	def __init__(self,play1="Player1",play2="Player2",numset=3,numgame=6,firstserve=1):
		global p1,p2,g1,g2,s1,s2,s,ts,tsc
		self.P1=play1
		self.P2=play2
		self.nos=numset
		self.nog=numgame
		self.fs=firstserve
		s=self.fs
		p1=0
		p2=0
		g1=0
		g2=0
		s1=0
		s2=0
		ts=0

	def __str__(self):
		if self.fs==1:
			matchdisplay=f'''{self.P1} Vs {self.P2}.
{self.nos} sets, {self.nog} games per set.
First serve to {self.P1}.'''
		else:
			matchdisplay=f'''{self.P1} Vs {self.P2}.
{self.nos} sets, {self.nog} games per set.
First serve to {self.P2}.'''
		return matchdisplay

	def __repr__(self):
		return f"{self.P1} {self.P2}, {self.nos}/{self.nog}, {self.fs}"

	def gstat(self):
		global p1,p2,g1,g2,s1,s2,s
		return p1,p2,g1,g2,s1,s2,s

	def tgstat(self):
		global p1,p2,ts
		return p1,p2,ts	
	
	def modify(self,ng1,ng2,ns1,ns2,ns):
		global g1,g2,s1,s2,s
		g1=ng1
		g2=ng2
		s1=ns1
		s2=ns2
		s=ns	

	def point1(self):
		global p1,p2,g1,g2,s1,s2,s,ts,tsc
		if g1==g2==self.nog:
			if p1==0 and p2==0:
				ts=s
				tsc=1
			tsap=ts
			p1+=1
			tsc+=1
			ts,tsc=tieserve_switch(ts,tsc,p1,p2)
			if p1>p2+1 and p1>=7:
				s1+=1
				if s1==self.nos//2+1:
					statement='Game, set, and match, {}.'.format(lastname(self.P1).title())
					g1,g2,p1,p2=0,0,0,0
				else:
					g1+=1
					statement='Game and {} set for {}, {} games to {}'.format(set_stat(s1+s2),lastname(self.P1).title(),g1,g2)
					g1,g2,p1,p2=0,0,0,0
					s=serve_switch(s)
					return statement
			else:
				if ts==1:
					if tsap==1:
						return '{} to {}, {} to serve.'.format(p1,p2,lastname(self.P1).title())
					else:
						return '{} to {}, {} to serve.'.format(p2,p1,lastname(self.P1).title())
				elif tsap==1:
					return '{} to {}, {} to serve.'.format(p1,p2,lastname(self.P2).title())
				else:
					return '{} to {}, {} to serve.'.format(p2,p1,lastname(self.P1).title())
		else:
			if (p1==45 and p2<45) or (p1==60 and p2==45):
				g1+=1
				if (g1==self.nog and g2<self.nog-1) or (g1==self.nog+1 and g2==self.nog-1):
					s1+=1
					if s1==self.nos//2+1:
						statement='Game, set, and match, {}.'.format(lastname(self.P1).title())
						g1,g2,p1,p2=0,0,0,0
						return statement
					else:
						statement='Game and {} set for {}, {} games to {}'.format(set_stat(s1+s2),lastname(self.P1).title(),g1,g2)
						g1,g2,p1,p2=0,0,0,0
						s=serve_switch(s)
						return statement
				else:
					if g1>g2:
						statement='Game: {}, {} leads: {} games to {}'.format(lastname(self.P1).title(),lastname(self.P1).title(),gm_stat(g1),gm_stat(g2))
					elif g2>g1:
						statement='Game: {}, {} leads: {} games to {}'.format(lastname(self.P1).title(),lastname(self.P2).title(),gm_stat(g2),gm_stat(g1))
					else:
						statement='Game: {}, {} games all'.format(lastname(self.P1).title(),g1)
					p1,p2=0,0
					s=serve_switch(s)
					return statement
			elif p1==45 and p2==60:
				p2=45
				return 'Deuce'
			else:
				p1+=15
				if p1<60 and p2<60:
					if p1<45 or p2<45:
						if p1!=p2:
							if s==1:
								return '{}-{}'.format(pt_stat(p1),pt_stat(p2))
							else:
								return '{}-{}'.format(pt_stat(p2),pt_stat(p1))
						else:
							return '{} all'.format(pt_stat(p1))
					else:
						return 'Deuce'
				elif p1==60:
					if p2==45:
						return 'Advantage {}'.format(lastname(self.P1).title())
				elif p1==45:
					return 'Advantage {}'.format(lastname(self.P2).title())
					
	def point2(self):
		global p1,p2,g1,g2,s1,s2,s,ts,tsc
		if g2==g1==self.nog:
			if p2==0 and p1==0:
				ts=s
				tsc=1
			tsap=ts
			p2+=1
			tsc+=1
			ts,tsc=tieserve_switch(ts,tsc,p1,p2)
			if p2>p1+1 and p2>=7:
				s2+=1
				if s2==self.nos//2+1:
					statement='Game, set, and match, {}.'.format(lastname(self.P2).title())
					g2,g1,p2,p1=0,0,0,0
				else:
					g2+=1
					statement='Game and {} set for {}, {} games to {}'.format(set_stat(s2+s1),lastname(self.P2).title(),g2,g1)
					g2,g1,p2,p1=0,0,0,0
					s=serve_switch(s)
					return statement
			else:
				if ts==1:
					if tsap==1:
						return '{} to {}, {} to serve.'.format(p1,p2,lastname(self.P1).title())
					else:
						return '{} to {}, {} to serve.'.format(p2,p1,lastname(self.P1).title())
				elif tsap==1:
					return '{} to {}, {} to serve.'.format(p1,p2,lastname(self.P2).title())
				else:
					return '{} to {}, {} to serve.'.format(p2,p1,lastname(self.P2).title())
		else:
			if (p2==45 and p1<45) or (p2==60 and p1==45):
				g2+=1
				if (g2==self.nog and g1<self.nog-1) or (g2==self.nog+1 and g1==self.nog-1):
					s2+=1
					if s2==self.nos//2+1:
						statement='Game, set, and match, {}.'.format(lastname(self.P2).title())
						g2,g1,p2,p1=0,0,0,0
						return statement
					else:
						statement='Game and {} set for {}, {} games to {}'.format(set_stat(s2+s1),lastname(self.P2).title(),g2,g1)
						g2,g1,p2,p1=0,0,0,0
						s=serve_switch(s)
						return statement
				else:
					if g1>g2:
						statement='Game: {}, {} leads: {} games to {}'.format(lastname(self.P2).title(),lastname(self.P1).title(),gm_stat(g1),gm_stat(g2))
					elif g2>g1:
						statement='Game: {}, {} leads: {} games to {}'.format(lastname(self.P2).title(),lastname(self.P2).title(),gm_stat(g2),gm_stat(g1))
					else:
						statement='Game: {}, {} games all'.format(lastname(self.P2).title(),g1)
					p2,p1=0,0
					s=serve_switch(s)
					return statement
			elif p2==45 and p1==60:
				p1=45
				return 'Deuce'
			else:
				p2+=15
				if p1<60 and p2<60:
					if p1<45 or p2<45:
						if p2!=p1:
							if s==1:
								return '{}-{}'.format(pt_stat(p1),pt_stat(p2))
							else:
								return '{}-{}'.format(pt_stat(p2),pt_stat(p1))
						else:
							return '{} all'.format(pt_stat(p1))
					else:
						return 'Deuce'
				elif p1==60:
					if p2==45:
						return 'Advantage {}'.format(lastname(self.P1).title())
				elif p1==45:
					return 'Advantage {}'.format(lastname(self.P2).title())		