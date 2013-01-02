#!/usr/bin/python
# -*- coding: utf8 -*-
import re,sys

def preg_match_all(pattern,string):
	compiled = re.compile(pattern)
	return re.findall(compiled,string)
	

# Exemplo de uso:
if __name__ == '__main__':
	string = """ 
		ola teste 123 testando essa bagaca.
		Ola teste 456 testando de novo.
		"""
	print preg_match_all('[0-9]+',string)
