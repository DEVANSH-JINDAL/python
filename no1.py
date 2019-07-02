def ran_bool(num,low,high):
    for x in range(low,high):
    	if num==x:
    		print True
    		break
    else:
    	if num >x:
    		print "greater"
    	else:
    		print "lesser"

ran_bool(11,1,10)
