# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())

res = 0

for num in range(user_input):
	res += str(num).count("3")
	res += str(num).count("6")
	res += str(num).count("9")

print(res)
