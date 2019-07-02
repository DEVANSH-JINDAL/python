#class circle(object):
#	pi=3.14
#	radius=1
#	def __init__(self,radius=1):
#		self.radius=radius
#		print "const"
#	def area(self):
#		return self.radius*self.radius*circle.pi
#	def setrad(self,radius):
#		self.radius=radius
#	def getrad(self):
#		return self.radius
class Base(object):
	def __init__(self):
		print "Base class"
	def fun(self):
		print "fun Base"

class child(Base):
	def __init__(self):
#		Base.__init__(self)
		print "child"
	def fun(self):
		print "fun child"
	def __str__(self):
		return "str"
	def __len__(self):
		return 5
	def __del__(self):
		print "deleted"
#c=Base()
c=child()
#c=Base()
print c
print len(c)
del c
print child.__doc__


q=9
del q
#print id(q)