def solution(n):
    answer = ""
    while n > 0:
        # 자릿수가 올라가는 것을 방지
        n -= 1
        answer = "124"[n%3] + answer 
        # 몫을 계산해서 다음 자릿수 연산을 위해
        n //= 3
        
    return answer

    