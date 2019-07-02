x=None
def func():
    global x
    print 'global x is: ', x
    x = "4g"
    print 'changed x to', x

print 'Before', x
func()
print 'outside of func is: ', x
