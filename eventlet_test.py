import eventlet
eventlet.monkey_patch()

import time	#nu ii modul built in, ii modul pus de eventlet

def count():
	for i in xrange(10):	#fata de range xrange doar genereaza, nu retine in memorie
		print i

worker = eventlet.spawn(count)
time.sleep(0)
worker.wait()
