# Q1
# def word_lengths(phrase):
# 		print map(len,phrase.split())


# word_lengths('How long are the words in this phrase')

#Q2
# def digits_to_num(digits):
#     print reduce(lambda x,y:x*10+y,digits)
    
# digits_to_num([3,4,3,2,1])

#Q3
# def filter_words(word_list, letter):
#     print filter(lambda x:x[0]==letter,word_list)


# l = ['hello','are','cat','dog','ham','hi','go','to','heart']
# filter_words(l,'h')

#Q4

# def concatenate(L1, L2, connector):
#     print [w1+connector+w2 for (w1,w2) in zip(L1,L2)]
# concatenate(['A','B'],['a','b'],'-')

#Q5

def d_list(L):
	
	print {item:count for count,item in enumerate(L) }


d_list(['a','b','c'])
{'a': 0, 'b': 1, 'c': 2}