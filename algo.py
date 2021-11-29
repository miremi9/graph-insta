from api2 import *


def main(pseudo,depth,backup=False):	
	try:
		if backup:
			do,todo = get_backup(pseudo)
		else:
			todo=get_followers(pseudo)
			do = set()
			do.add(pseudo)

		for i,name in enumerate(todo):	
			print(name)
			li=get_followers(name)
			if len(li) ==0:
				li = [name]
			save(name,li)
			do.add(name)
			print(f"Finish :{name},{len(li)}abonnements, {i} fait, {len(todo)} prevus ",)	
			
	except Exception as E:
		print(E)




def save(name:str,data:set):
	with open("data.csv","a") as f:
		for k in data:
			f.write(f"{name}:{k}\n")
	print("sauvegarde des data de :",name)


def get_backup(pseudo):
	with open("data.csv","r") as f:
		l_todo = set()
		do = set()
		for k in f.readlines():

			if f"{pseudo}:" in k:
				l_todo.add(k.split(":")[1].strip())

			name = k.split(":")[0]
			do.add(name)

	l_todo.difference_update(do)
	return do,l_todo
	
def get_data(pseudo):
	with open("data.csv","r") as f:
		do = list()
		line = f.readline()
		doing =line.split(":")[0]
		while line:
			while line.split(":")[0] ==doing:
				line = f.readline()
			do.append(doing)
			doing = line.split(":")[0]

	return do


main("__remi__m",3,backup=False)

