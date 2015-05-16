'''
def my_decorator(functie):
	def wrapper():
		print 'inainte de functie %s' % functie.func_name
		functie()
		print 'dupa functie %s' % functie.func_name
	return wrapper
'''
#def my_decorator(functie):
#	def wrapper(**kwargs):
#		print 'inainte de functie %s' % functie.func_name
#		functie(**kwargs)
#		print 'dupa functie %s' % functie.func_name
#	return wrapper
'''
def my_decorator(functie):
	def wrapper(*args, **kwargs):
		print 'inainte de functie %s' % functie.func_name
		functie(*args, **kwargs)
		print 'dupa functie %s' % functie.func_name
	return wrapper

def f():
	print 'Hello world fin f'

def f1(a):
	print a

f1 = my_decorator(f1)
'''
'''
def my_decorator(functie):
	def wrapper(*args, **kwargs):
		print 'inainte de functie %s' % functie.func_name
		functie(*args, **kwargs)
		print 'dupa functie %s' % functie.func_name
	return wrapper

def f():
	print 'Hello world fin f'

@my_decorator
def f1(a):
	print a

#f1 = my_decorator(f1)
'''

''' iar
def my_decorator(functie):
	def wrapper(*args, **kwargs):
		print 'inainte de functie %s' % functie.func_name
		functie(*args, **kwargs)
		print 'dupa functie %s' % functie.func_name
	return wrapper

def f():
	print 'Hello world fin f'

@my_decorator
def f1(a):
	print a
	raise Exception("my message")
'''
import functools

def my_decorator(functie):
	@functools.wraps(functie)
	def wrapper(*args, **kwargs):
		print 'inainte de functie %s' % functie.func_name
		functie(*args, **kwargs)
		print 'dupa functie %s' % functie.func_name
	return wrapper

def f():
	print 'Hello world fin f'

@my_decorator
def f1(a):
	print a
	raise Exception("my message")
