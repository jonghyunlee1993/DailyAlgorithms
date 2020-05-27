# 테스트 케이스는 통과했는데 제출은 실패함
# 최소 단위가 1이 아닐 때가 걸리는 것일까?

import numpy as np

def solution(n, money):
    # 배열 생성
    table = np.array([[0 for _ in range(n+1)] for _ in range(len(money))])
    # 가장 작은 단위로 만들 수 있는 경우의 수 
    table[0, :] = 1
    
    # 가장 작은 단위를 제외한 그 다음 단위의 동전
    for coin_type in range(1, len(money)):
        # 개수를 하나씩 늘려가면서  
        for coin_count in range(n + 1):
            # 남은 금액을 동전 종류로 나눌 수 있다면 경우의 수를 추가한다
            if coin_count >= money[coin_type]:
                table[coin_type, coin_count] = (table[coin_type-1, coin_count] + table[coin_type, coin_count - money[coin_type]]) % 1000000007
            # 남은 금액을 동전 종류로 나눌 수 없다면 경우의 수를 추가하지 않는다
            else:
                table[coin_type, coin_count] = table[coin_type-1, coin_count]
                
    return table[-1, -1]