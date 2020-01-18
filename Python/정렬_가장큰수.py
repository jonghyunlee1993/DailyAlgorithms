from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(lambda x: str(x), numbers))
    numbers = sorted(numbers, key=cmp_to_key(lambda a, b: -1 if a+b >= b+a else 1))
    print(numbers)
    answer = ''.join(numbers)

    return str(int(answer))

numbers = [6, 10, 2]
answer = solution(numbers)
print(answer)

# functools 의 cmp_to_key 함수는 원하는 조건으로 정렬해주는 함수
# 이 경우 텍스트끼리 합쳐진 값을 int로 바꾸어 비교한 후에 해당 결과가 크냐 작냐에 따라서 앞으로 혹은 뒤로 보내줌
# -1인 경우에 앞으로 보내고 1인 경우에 뒤로 보내서 정렬한다
# 최초에 numpy를 이용해서 비교하려 하였으나 너무 비효율적이었음

