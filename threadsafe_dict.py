import threading

def apply_lock(func):
	def wrapper(inst, *args, **kwargs):	
		with inst._lock:
			return func(inst,*args , **kwargs)
	return wrapper

class threadsafeDict(dict):
	#metoda incepe cu _ pt ca ii considerata privata prin conventie
	_lock = threading.Lock()

	@apply_lock
	def __getitem__(self, key):
		with self._lock:
			super(threadsafeDict, self).__getitem__(key)
	
	@apply_lock
	def __setitem__(self, key, value):
		with self._lock:
			super(threadsafeDict, self).__setitem__(key, value)




'''
with open('nume_fisier', 'w') as f:
	f.write('test') 
'''

mydict = threadsafeDict()
mydict['test']=10
print mydict['test']
