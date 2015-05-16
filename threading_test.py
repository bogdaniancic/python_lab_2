import threading
from Queue import Queue

myqueue= Queue() 

def count():
	for i in xrange(10):	#fata de range xrange doar genereaza, nu retine in memorie
		myqueue.put(i)

#folosesti thread-uri cand ai operatii ce dureaza mult timp
#sau cand ai un daemon
workers = []

for i in xrange(3):
	worker = threading.Thread(target = count)
	worker.setDaemon(True)
	worker.start()
	workers.append(worker)

#un thread pornit ca si daemon nu poate porni alti daemoni
#join asteapta pana un worker si-a terminat executia
#daca si-a terminat deja executia se refera la cel curent
for worker in workers:
	if worker != threading.current_thread:
		worker.join()

while not myqueue.empty():
	print myqueue.get()
