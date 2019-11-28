# def gen(num):
# 	for x in range(num):
# 		yield x**3
# for y in gen(10):
# 	print y

# '''efeerg
# gfegw
# wfg'''

# def fibonnaci(n):
# 	a=1
# 	b=1
# 	for x in range(n):
# 		yield a
# 		c=a
# 		a=b
# 		b=c+b
# 		print a,b
# 		a,b=b,a+b
# for x in fibonnaci(2):
# 	print x
# 	print "hi"

def simple_gen():
    for x in range(4):
        yield x
# Assign simple_gen 
g = simple_gen()

print next(g)
print next(g)
print next(g)
print next(g)
