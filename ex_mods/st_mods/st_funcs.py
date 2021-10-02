#

def lastname(C):
	return C.split()[-1]

def pt_stat(pt):
    dictiopt={0:'Love',15:'Fifteen',30:'Thirty',45:'Fourty'}
    return dictiopt[pt]

def gm_stat(g):
	dictiogmnums={}
	translate=['love','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
	for i in range(len(translate)):
		dictiogmnums[i]=translate[i]
	return dictiogmnums[g]

def set_stat(set):
	translatedset=['first','second','third','fourth','fifth']
	dictiosetnums={}
	for i in range(1,5):
		dictiosetnums[i]=translatedset[i-1]
	return dictiosetnums[set]

def serve_switch(serve):
	if serve==1:
		serve=2
	else:
		serve=1
	return serve

def tieserve_switch(tieserve,tieservecount,p1,p2):
	if tieservecount==2:
		if tieserve==1:
			tieserve=2
		else:
			tieserve=1
		tieservecount=0
	return tieserve,tieservecount

def p(p):
	a=p
	if a==45:
		a=40
	elif a==60:
		a='Ad'
	return a