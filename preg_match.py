import re,sys
"""
pattern = expressão regular de entrada
string = string a ser analisada
"""
def preg_match(pattern,string):
	compiled = re.compile(pattern)
	result = re.search(compiled,string)
	if result.groups() != ():
		return result.groups()
	else:
		return result.group(0)

if __name__ == '__main__':
	string = "<a href='http://teste.com.br'>teste 123</a>"
	# Exemplo 1
	result = preg_match('[0-9]+',string)
	print "Retorno exemplo 1:"
	print result,"\n"
	# Exemplo 2
	result = preg_match('<a href=(.*?)>(.*?)</a>',string)
	print "Retorno exemplo 2:"
	print result,"\n"
