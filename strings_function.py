"""
addslashes
"""
def addslashes(string):
	return string.replace('"',"\\\"").replace("'","\\\'")


if __name__ == '__main__':
	print addslashes("o'neil")

