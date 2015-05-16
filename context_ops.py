'''
fd = open('myfile.txt', 'w')
fd.write('test')
fd.close()
'''

'''
with open('myfile.txt', 'w') as fd:
	fd.write('test')
'''

import contextlib

@contextlib.contextmanager
def myopen(*args, **kwargs):
	fd = None

	try:
		print 'opening file'
		fd = open(*args, **kwargs)
		yield fd
	except Exception as exc:
		print "Got exception %s" % exc
	finally:
		if fd:
			print 'closing file'
			fd.close()				

with myopen('myfile.txt', 'w') as fd:
	fd.write('test')

