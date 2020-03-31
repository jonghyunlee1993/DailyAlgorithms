def solution(n, times):
    # 오른쪽은 가장 최악의 경우를 가정
    # 오래 걸리는 심사관이 모든 입국심사를 진행할 때
    left, right = 1, max(times) * n
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            # 시간 내 처리 가능한 모든 인원
            people += mid // time
            
            if people >= n:
                break
        
        # 목표량 처리가 가능할 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 목표량 처리가 불가능할 경우
        else:
            left = mid + 1
            
    return answer