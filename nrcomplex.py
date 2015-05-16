class NrComplex(object):
	def __init__(self, a ,b):
		self.a = a
		self.b = b

	def __add__(self, second_number):
		return NrComplex(self.a + second_number.a, self.b + second_number.b)

	def __repr__(self):
		return "%s + i * %s" % (self.a, self.b)


