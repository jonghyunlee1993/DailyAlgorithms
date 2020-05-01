def solution(n, a, b):
    count = 0

    # a, b가 동일한 경기 번호를 갖으면 중단
    while a != b:
    	# 경기 번호는 2명이 동일한 번호를 갖기 때문에 // 2 취함
        a = (a + 1) // 2
        b = (b + 1) // 2  
        
        count += 1

    return count