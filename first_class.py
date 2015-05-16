class MyClass(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def my_method(self):
		print self.a, self.b

class MyClass1(object):
	def __init__(self, e):
		self.e = e

	def my_method(self):
		print "My Method from class1"

class MyClassExtended(MyClass, MyClass1):
	def __init__(self, a, b, c):
		super(MyClassExtended, self).__init__(a,b)	#apeleaza constructorul din super class
		self.c = c 
	
	#def my_method(self): #daca nu defineam aveam my_method de sus
	#	super(MyClassExtended, self).my_method()
	#	print self.c
		


