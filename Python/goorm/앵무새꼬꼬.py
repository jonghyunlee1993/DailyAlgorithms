# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
length = int(input())

for i in range(length):
	res = str()
	sent = str(input())
	
	for char in sent:
		if char.count("A") or char.count("a"):
			res += char
		elif char.count("E") or char.count("e"):
			res += char
		elif char.count("I") or char.count("i"):
			res += char
		elif char.count("O") or char.count("o"):
			res += char
		elif char.count("U") or char.count("u"):
			res += char
	
	if not res:
		res = "???"
		
	print(res)