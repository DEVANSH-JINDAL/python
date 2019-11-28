# s="Global Variables"
# def fun():
# 	print locals()
# print globals()#["s"]
# #print locals()

# def hello(name="josh"):
# 	print "hello",name
# hello()
# hj=hello
# hj()
# print hj
# print hello
# del hello
# hj()


# def hello():
# 	print "hello"
# def hi(fun):
# 	print "hi"
# 	fun()
# hi(hello)


def new_deco(func):
	def hello():
		print "before func"
		func()
		print "after func"
	return hello
# def need():
# 	print "need of decorator"
# need()
# need=new_deco(need)
# need()


@new_deco
def need():
	print "need of decorator"
def need1():
	print "need of decorator"
need()
need1()