#try:
#f=open("new.txt","r")
#f.write("fsgdhf")
#f.read()
#except IOError:
#	print "Input/Output Error"
#else:
#	print "success"
#f.close()
# try:
# 	a=10/0
# except:
# 	print "error"
# else:
# 	print a
# finally:
# 	print"hi"
def askint():
        try:
            val = int(raw_input("Please enter an integer: "))
        except:
            print "Looks like you did not enter an integer!"
            
        finally:
            print "Finally, I executed!"
        print val  
#askint()