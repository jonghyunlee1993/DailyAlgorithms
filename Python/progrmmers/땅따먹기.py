# 자기 자신과 동일하지 않은 인덱스의 최댓값을 더하는 방식으로 누적

def solution(land):
	line = len(land)
	for i in range(line-1):
		land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
		land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
		land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
		land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
	return max(land[i+1])

# 맨 처음 생각했던 풀이
# 단순하게 테스트 케이스만 고려함
# 가장 큰 수가 자기 자신의 뒤에 있을 경우에는 틀리게 됨

def solution(land):
    score = 0
    for i, line in enumerate(land):
        if not i == 0:
            line[tile] = 0
        
        tile = line.index(max(line))
        score += max(line)
    
    return score