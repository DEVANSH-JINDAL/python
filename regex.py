import re
# def fin(patterns,text):
# 	print re.findall(patterns,text)
# 'sd*',          # s followed by zero or more d's
# 'sd+',          # s followed by one or more d's
# 'sd?',          # s followed by zero or one d's
# 'sd{3}',        # s followed by three d's
# 'sd{2,3}'
# fin("sd*","sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd...d")

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print 'Searching the phrase using the re check: %r' %pattern
        print re.findall(pattern,phrase)
        print '\n'
test_phrase = 'This 78 is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
				]

multi_re_find(test_patterns,test_phrase)