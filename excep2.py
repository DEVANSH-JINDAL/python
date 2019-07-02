# def askint():
#         try:
#             val = int(raw_input("Please enter an integer: "))
#         except:
#             print "Looks like you did not enter an integer!"
#             val = int(raw_input("Try again-Please enter an integer: "))
#         finally:
#             print "Finally, I executed!"
#         print val 
# askint()
#homework
# for i in ['a','b','c']:
#     try:
#     	print i**2
#     except:
#     	print "error"
#     else:
#     	print "success"
# print "yess"



# Write a function that asks for an integer and prints the square of it. Use a while loop with a try,except
# , else block to account for incorrect inputs.

def ask():
	while True:
		try:
			a=int(raw_input("enter a number: "))
		except:
			print "not an integer"
			#continue
		else:
			print a**2
			break
		
ask()

