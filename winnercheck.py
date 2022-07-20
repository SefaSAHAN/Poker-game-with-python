#diamonds (♦), clubs (♣), hearts (♥) and spades (♠)
import more_itertools as mit
import random

symbol=["♦","♣","♥","♠"]
counts=list(range(1,14))
deck=[]
for i in symbol:
	for j in counts:
		if j==1:
			j="Ace"
			deck.append(str(j)+i)
		elif j==11:
			j="Jack"
			deck.append(str(j)+i)
		elif j==12:
			j="Queen"
			deck.append(str(j)+i)
		elif j==13:
			j="King"
			deck.append(str(j)+i)
		else:
			deck.append(str(j)+i)

playerlist0=list(range (1,5))
playerlist=[]
for i in playerlist0:
	playername="player"+str(i)
	playerlist.append(playername)
boardcards=[]
def board(a):
	boardcards.extend(random.sample(deck,a))
	for j in boardcards:
		try:
			deck.remove(j)
		except:
			pass
	print("board:",boardcards)
	return boardcards


playerhands=[]
for i in playerlist:
	c= random.sample(deck, 2)
	playerhands.append(c)
	for j in c:
		deck.remove(j)
playercardsdic= dict(zip(playerlist,playerhands))
print(playercardsdic)
board(5)

playercontdic={}
def resultcardsdic():
	for i,j in playercardsdic.items():
			a=[]
			a.extend(j)
			a.extend(boardcards)
			playercontdic[i]=a

def dublicatecheckdic():
	for e, i in playercontdic.items():
		kontroldublicate=[]
		for j in i:
			a= j[:-1]
			if a=="Ace":
				a=14
			elif a=="King":
				a=13
			elif a=="Queen":
				a=12
			elif a=="Jack":
				a=11
			try:
				a=int(a)
			except:
				pass
			kontroldublicate.append(a)		
		playercontdic[e]=kontroldublicate

	for d,i in playercontdic.items():
		e={k:i.count(k) for k in set(i)}
		playercontdic[d]=e

controlelement=False

def royalflush():
	global controlelement
	resultcardsdic()
		
	for i ,j in playercontdic.items():
		royalclubs=["Ace♣","King♣","Queen♣","Jack♣","10♣"]
		a=[]
		a.extend(j)
		for element in royalclubs:
			if element in a:
				a.remove(element)
		x=len(a)
		if x==2:
			print(i, 'is royalflush')
			controlelement=True
		
	for i ,j in playercontdic.items():
		royaldiamonds=["Ace♦","King♦","Queen♦","Jack♦","10♦"]
		a=[]
		a.extend(j)
		for element in royaldiamonds:
			if element in a:
				a.remove(element)
		x=len(a)
		if x==2:
			print(i, 'is royalflush')
			controlelement=True
	
	
	for i ,j in playercontdic.items():
		royalhearts=["Ace♥","King♥","Queen♥","Jack♥","10♥"]
		a=[]
		a.extend(j)
		for element in royalhearts:
			if element in a:
				a.remove(element)
		x=len(a)
		if x==2:
			print(i, 'is royalflush')
			controlelement=True
	
	
	for i ,j in playercontdic.items():
		royalspades=["Ace♠","King♠","Queen♠","Jack♠","10♠"]
		a=[]
		a.extend(j)
		for element in royalspades:
			if element in a:
				a.remove(element)
		x=len(a)
		if x==2:
			print(i, 'is royalflush')
			controlelement=True
royalflush()


def flushstraight():
	global controlelement
	resultcardsdic()
	e=0
	f=0
	g=0
	h=0	
	for j in boardcards:
		i=j[-1]
		if i=="♣":
			e+=1
		elif i=="♥":
			f+=1
		elif i=="♠":
			g+=1
		else:
			h+=1
	if e>=3:
		symbol="♣"
	if f>=3:
		symbol="♥"
	if g>=3:
		symbol="♠"
	if h>=3:
		symbol="♦"
	else:
		symbol='&'
	for i,j in playercontdic.items():
		b=[]
	
		for k in j:
			if k[-1]==symbol:
				b.append(k)
		playercontdic[i]=b	
			
			
	for e,i in playercontdic.items():
		kontroldublicate=[]
		for j in i:
			a= j[:-1]
			kontroldublicate.append(a)		
		playercontdic[e]=kontroldublicate

	e=1
	for i in playercontdic.values():
		newliste=[]
		for j in i:
			if j=="Ace":
				newliste.append(1)
				newliste.append(14)
			elif j=="King":
				newliste.append(13)
			elif j=="Queen":
				newliste.append(12)
			elif j=="Jack":
				newliste.append(11)
			try:
				newliste.append(int(j))
			except:
				pass
		newliste.sort(reverse=True)
		playercontdic["player{}".format(e)]=newliste
		e+=1
	f=1	
	for i in playercontdic.values():
		newliste=[]
		g=0
		for j in i:
			j-=g
			newliste.append(j)
			g-=1
		playercontdic["player{}".format(f)]=newliste
		f+=1
	d=1
	for i in playercontdic.values():
		e={k:i.count(k) for k in set(i)}
		playercontdic["player{}".format(d)]=e
		d+=1
	d=1
	sonuçdict={}
	for i in playercontdic.values():
		for j in i.values():
			if j>=5:
				controlelement=True
				print("player{}:flushstraight".format(d))
				z = [key  for (key, value) in playercontdic["player{}".format(d)].items() if value>= 5]
				sonuçdict["player{}".format(d)]=z[0]		
		d+=1
	try:
		max_key = max(sonuçdict, key=sonuçdict.get)
		print(max_key,"is winner with higher flushstraight")
	except:
		pass

if controlelement==False:
	flushstraight()


def fourofaking():
	global controlelement
	resultcardsdic()
	dublicatecheckdic()

	winnercheck={}
	for i,j in playercontdic.items():	
		for k,l in j.items():
			if l==4:
				winnercheck[i]=k
	try:
		key = max(winnercheck, key = lambda z: winnercheck[z])
		print('{} is winner with higher <{}> four of a king'.format(key,winnercheck[key]))
	except:
		pass

if controlelement==False:
	fourofaking()

def fullhouse():
	global controlelement
	resultcardsdic()
	dublicatecheckdic()

	winnercheck={}
	for d,i in playercontdic.items():
		for j,k in i.items():
			x=0
			list1=[]
			if k==3:
				for l,m in i.items():
					if m==2:
						list1.append(l)	
					if m==3:
						list1.append(l)
						x+=1
				a=len(list1)
				if a>1:
					controlelement=True
					try:
						winnercheck[d]=max(list1)
					except:
						pass				
	
	try:
		key = max(winnercheck, key = lambda z: winnercheck[z])
		print('{} is winner with higher <{}> fullhouse'.format(key,winnercheck[key]))
	except:
		pass

if controlelement==False:
	fullhouse()


def flushcheck():
	global controlelement
	controldict1={}
	winnercheck={}
	resultcardsdic()
	winnercheck={}	
	for k,v in playercontdic.items():
		kontrolflush=[]
		for j in v:
			a=j[-1]
			kontrolflush.append(a)
		controldict1[k]=kontrolflush	
	for k,v in controldict1.items():
		e=0
		f=0
		g=0
		h=0	
		for j in v:
			if j=="♣":
				e+=1
			elif j=="♥":
				f+=1
			elif j=="♠":
				g+=1
			else:
				h+=1
		if e>4 or f>4 or g>4 or h>4:
			controlelement=True	
			winnercheck[k]=playercontdic[k]
	
	for e, i in winnercheck.items():
		kontroldublicate=[]
		for j in i:
			a= j[:-1]	
			if a=="Ace":
				a=14
			elif a=="King":
				a=13
			elif a=="Queen":
				a=12
			elif a=="Jack":
				a=11
			try:
				a=int(a)
			except:
				pass
			kontroldublicate.append(a)		
		winnercheck[e]=kontroldublicate
	if len(winnercheck)==1:
		for i in winnercheck.keys():
			print(i,' is winner with flush')

	elif len(winnercheck)>1:
		def whowin(l1,l2):
		    un = sorted(list(set(l1)^set(l2)))
		    if not bool(un): return -1
		    return 0 if un[-1] in l1 else 1

		def calc_points(winnercheck):
		    points = {i:0 for i in winnercheck}
		    checked = []
		    for i1,v1 in winnercheck.items():
		        for i2,v2 in winnercheck.items():       
		            if not i1 is i2 and not (i2,i1) in checked:
		                checked+=[(i1,i2)]             
		                if whowin(v1,v2):
		                    points[i2]+=1
		                else:
		                    points[i1]+=1 
		    return points
		
		def winner(points:dict):
		    return max(points.keys(),key=lambda x:points[x])
		try:
			print(winner(calc_points(winnercheck)),'is winner with higher flush ')
		except:
			pass
	
if controlelement==False:
	flushcheck()


def straight():
	global controlelement
	playercontdic={}
	resultdict={}
	d=0
	for i,j in playercardsdic.items():
		a=[]
		kontroldublicate=[]
		a.extend(j)
		a.extend(boardcards)
		for j in a:
			b= j[:-1]
			kontroldublicate.append(b)
		my_finallist = [j for k, j in enumerate(kontroldublicate) if j not in kontroldublicate[:k]]
		newliste=[]
		for j in my_finallist:
			if j=="Ace":
				newliste.append(1)
				newliste.append(14)
			elif j=="King":
				newliste.append(13)
			elif j=="Queen":
				newliste.append(12)
			elif j=="Jack":
				newliste.append(11)
			try:
				newliste.append(int(j))
			except:
				pass
		newliste.sort()	

		grplist = [list(group) for group in mit.consecutive_groups(newliste)]
	
		for j in grplist:
			if len(j)>4:
				controlelement=True
				playercontdic[i]=j
				resultdict[i]=max(j)

	try:
		key = max(resultdict, key = lambda z: resultdict[z])
	except:
		pass
	winnercheck={}

	for i,j in resultdict.items():
		if j==resultdict[key]:
			d+=1
			winnercheck[i]=playercontdic[i]
	if d==1:
		print('{} is winner with higher straight'.format(key,resultdict[key]))
	if d>1:
		a=[]
		for i in winnercheck.keys():
			a.append(i)
		print('{} are winner with same straight'.format(a))
		
if controlelement==False:
	straight()


def threeofakind():
	global controlelement
	resultcardsdic()
	dublicatecheckdic()

	winnercheck={}
	for d,i in playercontdic.items():
		for j,k in i.items():
			
			list1=[]
			if k==3:
				controlelement=True
				list1.append(j)
				winnercheck[d]=j
	try:
		key = max(winnercheck, key = lambda z: winnercheck[z])
		key2=winnercheck[key]
	except:
		pass

	c=0
	for i,j in winnercheck.items():
		if j==key2:
			c+=1
	
	if c==1:
		try:
			key = max(winnercheck, key = lambda z: winnercheck[z])
			print('{} is winner with higher <{}> three of a kind'.format(key,winnercheck[key]))
		except:
			pass
	winnercheck2={}
	winnercheck3={}
	if c>1:
		for i,j in playercontdic.items():
			list7=[]
			for k,l in j.items():
				if l==3:
					winnercheck2[i]=j

		for i,j in winnercheck2.items():
			list7=[]
			for k,l in j.items():
				list7.append(k)
			winnercheck3[i]=list7

		def whowin(l1,l2):
		    un = sorted(list(set(l1)^set(l2)))
		    if not bool(un): return -1
		    return 0 if un[-1] in l1 else 1

		def calc_points(winnercheck3):
		    points = {i:0 for i in winnercheck3}
		    checked = []
		    for i1,v1 in winnercheck3.items():
		        for i2,v2 in winnercheck3.items():       
		            if not i1 is i2 and not (i2,i1) in checked:
		                checked+=[(i1,i2)]             
		                if whowin(v1,v2):
		                    points[i2]+=1
		                else:
		                    points[i1]+=1 
		    return points
		
		def winner(points:dict):
		    return max(points.keys(),key=lambda x:points[x])
		try:
			print(winner(calc_points(winnercheck3)),'is winner with higher three of a kind card')
		except:
			pass

if controlelement==False:
	threeofakind()

def twopair():
	global controlelement
	resultcardsdic()
	dublicatecheckdic()

	winnercheck={}
	for d,i in playercontdic.items():
		for j,k in i.items():
			x=0
			list1=[]
			if k==2:
				for l,m in i.items():
					if m==2:
						list1.append(l)	
				a=len(list1)
				if a>1:
					controlelement=True
					try:
						winnercheck[d]=max(list1)
					except:
						pass
	try:
		key = max(winnercheck, key = lambda z: winnercheck[z])
		print('{} is winner with higher <{}> twopair'.format(key,winnercheck[key]))
	except:
		pass

if controlelement==False:
	twopair()

controlelement3=False
controlelement2=False
dictionary4={}
def onepair():
	global dictionary4
	global controlelement
	global controlelement2
	global controlelement3
	resultcardsdic()
	dublicatecheckdic()
		
	dictionary1={'player1':0}
	for d,i in playercontdic.items():
		for j,k in i.items():
			if k==2:
				controlelement=True
				controlelement3=True
				try:
					key1= max(dictionary1, key = lambda z: dictionary1[z])
				except:
					pass
				try:
					if j>dictionary1[key1]:
						dictionary1.clear()
						dictionary1[d]=j
					if j==dictionary1[key1]:
						dictionary1[d]=j
				except:
					pass

	dictionary2={'player1':0}
	dictionary3={'player1':[],'player2':[],'player3':[],'player4':[],'player5':[],'player6':[],'player7':[],'player8':[],'player9':[]}
	
	if len(dictionary1)==1:
		for i,j in dictionary1.items():
			if j>0:
				print (i, 'is winner with higher one pair.')	
		
	elif len(dictionary1)>1:
		controlelement3=True
		controlelement2=True
		for i,j in dictionary1.items():
			dictionary2[i]=playercontdic[i]
		for i,j in dictionary2.items():
			newlist3=[]
			
			try:
				for k,l in j.items():
					newlist3.append(k)
				if len(newlist3)>0:
					dictionary4[i]=newlist3	
			except:
				pass

		def whowin(l1,l2):
		    un = sorted(list(set(l1)^set(l2)))
		    if not bool(un): return -1
		    return 0 if un[-1] in l1 else 1

		def calc_points(dictionary4):
		    points = {i:0 for i in dictionary4}
		    checked = []
		    for i1,v1 in dictionary4.items():
		        for i2,v2 in dictionary4.items():       
		            if not i1 is i2 and not (i2,i1) in checked:
		                checked+=[(i1,i2)]             
		                if whowin(v1,v2):
		                    points[i2]+=1
		                else:
		                    points[i1]+=1 
		    return points
		
		def winner(points:dict):
		    return max(points.keys(),key=lambda x:points[x])
		try:
			print(winner(calc_points(dictionary4)),'is winner with higher one pair ')
		except:
			pass	
	
if controlelement==False:
	onepair()

resultcardsdic()
dublicatecheckdic()

def whowin(l1,l2):
    un = sorted(list(set(l1)^set(l2)))
    if not bool(un): return -1
    return 0 if un[-1] in l1 else 1

def calc_points(playercontdic):
    points = {i:0 for i in playercontdic}
    checked = []
    for i1,v1 in playercontdic.items():
        for i2,v2 in playercontdic.items():       
            if not i1 is i2 and not (i2,i1) in checked:
                checked+=[(i1,i2)]             
                if whowin(v1,v2):
                    points[i2]+=1
                else:
                    points[i1]+=1 
    return points

if controlelement==False:
	def winner(points:dict):
	    return max(points.keys(),key=lambda x:points[x])
try:
	if controlelement3==True:
		pass
	else:
		print(winner(calc_points(playercontdic)),'is winner with higher card')
except:
	pass