# def fahrenheit(T):
#     return ((float(9)/5)*T + 32)

temp = [0, 22.5, 40,100]
# f_temp=map(fahrenheit,temp)
# print f_temp

#print map(lambda T:((float(9)/5)*T + 32),temp)

#new

l1=[1,2,3,4,5]
l2=[2,3,4,5,6]
mapl=map(lambda x,y:x*y,l1,l2)
print(mapl)