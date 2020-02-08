def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.extend([num])
    if not answer:
        answer.extend([-1])
    return sorted(answer)