def solution(arrangement):
    arrangement = arrangement.replace('()', 'l')
    answer = 0
    stick = 0
    for s in arrangement:
        if s == "(":
            stick += 1
        elif s == "l":
            answer += stick
        elif s == ")":
            stick -= 1
            answer += 1
    
    return answer