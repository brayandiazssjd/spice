from Controller import Controller
p = Controller().package("Hello, my name is Brayan and I am testing this method", 8)
for q in p:
	print(q.playload)