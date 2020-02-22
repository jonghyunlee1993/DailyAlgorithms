# stack을 이용한 정석적 풀이
# 효율성 테스트도 통과 가능

def solution(s):
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        
    if not stack:
        return True
    else:
        return False

# string의 replace 를 이용한 풀이
# 효율성 테스트를 통과하지 못함

def solution(s):
	for i in range(len(s)):
		s = s.replace("()", "")
		if not s:
			return True

	return False

