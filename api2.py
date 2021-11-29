import instaloader
import time
L = instaloader.Instaloader()
#new comment
login = [("remire6__","WSkv23XJ32Wpctf"),("__remi__m","9jra238tgiMLDag"),("mimire9_","Yv7qbTmj7z7NZni")]

# Login or load session
L.login(*login[1])        # (login)


def get_followers(id):
	profile = instaloader.Profile.from_username(L.context, id)
	f = profile.get_followees()
	li = set()
	for k in f:
		li.add(k.username)
	print(len(li))
	time.sleep(5)
	return li
