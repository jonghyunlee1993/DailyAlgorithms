def solution(n):
    pattern = "수박"
    if n % 2 == 0:
        answer = pattern * int(n / 2)
    else:
        answer = pattern * int(n / 2) + "수"
    return answer