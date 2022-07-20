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

while True:
	try:
		playercount=int(input("how many players on table:"))
		break
	except ValueError:
		        print("Oops!  That was no valid input. try again?")

playerlist0=list(range (1,playercount+1))
playerlist=[]
for i in playerlist0:
	playername="player"+str(i)
	playerlist.append(playername)
boardcards=[]

playerbudgetsdic={}

def budget():
	global playerbudgetsdic
	playersbudget=[]
	a=int(input("sellect budget type\n1:same for everyone\n2:different for everyone:"))
	if a==1:
		playersbudget.extend([200 for i in range(playercount)])
		playerbudgetsdic= dict(zip(playerlist,playersbudget))
		print(playerbudgetsdic)
	elif a==2:
		d=0
		while d<playercount:
			e=int(input("{} budget:".format(playerlist[d])))
			playersbudget.append(e)
			d+=1
		playerbudgetsdic= dict(zip(playerlist,playersbudget))
		print(playerbudgetsdic)
	else:
		a/0

while True:
	try:
		budget()
		break
	except ValueError:
		print("Oops!  That was no valid input. try again?")

totalmoney=sum(playerbudgetsdic.values())

def pot():
	pot= totalmoney-sum(playerbudgetsdic.values())
	print('pot is {}$'.format(pot))

playerhands=[]
for i in playerlist:
	c= random.sample(deck, 2)
	playerhands.append(c)
	for j in c:
		deck.remove(j)
playercardsdic= dict(zip(playerlist,playerhands))
print(playercardsdic)

def board(a):
	boardcards.extend(random.sample(deck,a))
	for j in boardcards:
		try:
			deck.remove(j)
		except:
			pass
	print("board:",boardcards)
	return boardcards


playerbetdic={}
def bet():
	freelist=[]
	newlist=[]
	for i in playerlist:
		e=input("{} bet or press 'q' to resign :".format(i))
		if e=="q":
			print("{} is resigned".format(i))
			playerbetdic[i]='resigned'	
		else:
			freelist.append(int(e))
			playerbetdic[i]=int(e)
			try:
				for j in freelist:
					newlist.append(int(j))
					max_value=max(newlist)
			except:
				pass
			f=int(e)
			while f<max_value:
				e=input("{} to continue minimum bet is {} or push 'q' button to resign:".format(i,max_value))
				if e=="q":
					print("{} is resigned".format(i))
					playerbetdic[i]="resigned"
					break	
				else:
					f=int(e)
					newlist.append(int(e))
					playerbetdic[i]=int(e)


while True:
	try:
		bet()
		break
	except ValueError:
		print("Oops!  That was no valid input. try again?")

def reducebudget():
	global playerbudgetsdic
	global playerbetdic
	for i,j  in playerbudgetsdic.items():
		try:
			j-=playerbetdic[i]
			playerbudgetsdic[i]=j
		except:
			pass
	return playerbudgetsdic

reducebudget()


def betcheck():
	newliste=[]
	for i in playerbetdic.values():
		try:
			newliste.append(int(i))
		except:
			pass
	
	for j , k  in playerbetdic.items():
		max_value2=max(newliste)
		if k=="resigned":
			pass
		else:
			f=int(k)
			while f<max_value2:
				k=input("{} to continue minimum bet is {}, or push 'q' button to resigned:".format(j,max_value2))
				if k=="q":
					print(j," is resigned")
					playerbetdic[j]="resigned"
					break	
				else:
					f=int(k)
					playerbudgetsdic[j]-=f-playerbetdic[j]
					playerbetdic[j]=f
					newliste.append(f)

betcheck()
betcheck()
board (3)
print(playerbetdic)
print (playerbudgetsdic)
pot()
def playerlistcheck():
	for i, j in playerbetdic.items():
		if j=="resigned":
			playerlist.remove(i)
playerlistcheck()

playerbetdic={}
bet()
reducebudget()
newliste=[]
betcheck()
betcheck()
board (1)
print(playerbetdic)
print (playerbudgetsdic)
pot()
playerlistcheck()

playerbetdic={}
bet()
reducebudget()
newliste=[]
betcheck()
betcheck()
board (1)
print(playerbetdic)
print (playerbudgetsdic)
pot()
playerlistcheck()

playerbetdic={}
bet()
reducebudget()
newliste=[]
betcheck()
betcheck()
print(playerbetdic)
print (playerbudgetsdic)
pot()



input()

