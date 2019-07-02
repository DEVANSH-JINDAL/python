#l=[1,2,3,4,5,5,5,5,5]
#print l.count(5)
#print type(5)
#class sample(object):
#	pass
#x=sample()
#print type(x)
#y=None
#print type(y)
class Dog(object):
	type="Dog"
	def __init__(self,breed,name):
		self.breed=breed
		self.name=name
sam=Dog("pug","sho")
print sam.breed
print sam.name
print sam.type
