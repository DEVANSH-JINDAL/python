#reduce
l=[1,2,3,4,5,6,7]
print reduce(lambda x,y:x if x>y else y,l)

#x%2==0 will be checked on last index
lst=reduce(lambda x,y:y%2==0,l)	
print lst

#filter
print filter(lambda x:True if x%2==0 else False,l)
print filter(lambda x:x%2==0,l)


#enumerate
for count,item in enumerate(l):
    if count >= 2:
        break
    else:
        print item

print "\n"
print all(l)