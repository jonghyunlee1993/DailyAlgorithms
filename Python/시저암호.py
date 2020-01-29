import string

def solution(s, n):
	answer = ""

	lower = string.ascii_lowercase * 2
	upper = string.ascii_uppercase * 2

	for letter in s:
		if letter.isspace():
			answer += " "
		elif letter.isupper():
			answer += upper[upper.index(letter) + n]
		elif letter.islower():
			answer += lower[lower.index(letter) + n]

	return answer

s = "A B Cd"
n = 1
res = solution(s, n)
print(res)