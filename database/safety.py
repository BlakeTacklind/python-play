import re

alphanum = re.compile('[^\w]')
anANDspace = re.compile('[^\w ]')
notDigit = re.compile('[\D]')

def isAlphaStr(str):
	if(alphanum.search(str) == None):
		return True
	
	return False

def isAlphaSpaceStr(str):
	if(anANDspace.search(str) == None):
		return True
	
	return False

def isDigitStr(str):
	if(notDigit.search(str) == None):
		return True
	
	return False

# def is_json(myjson):
# 	try:
# 		json_object = json.loads(myjson)
# 	except ValueError:
# 		return False
# 	return True

def inDict(d, key):
	return key in d