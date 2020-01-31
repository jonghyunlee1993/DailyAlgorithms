def solution(x, n):
    if x * n == 0:
        answer = list(map(int, str(0) * n))
    elif x * n > 0: 
        answer = list(range(x, x*n + 1, x))
    else:
        answer = list(range(x, x*n - 1, x))
    return answer