# 빠리의 택시 운전사 블로그 참고
# 규칙 찾아서 해당 규칙 적용
# red의 가로, 세로 최대화 후 brown의 크기 도출 

def solution(brown, red):
    for a in range(1, int(red**0.5)+1):
        if not red % a:
            b = red // a
            if 2*a + 2*b + 4 == brown:
                return [b+2, a+2]

# 테스트 케이스 오류

def solution(brown, red):
    tiles = int(brown) + int(red)
    
    row = 1
    col = tiles
    
    while True:
        row += 1
        col = tiles / row
        
        if row == int(row) and col == int(col) and row >= col:
            break
        
    return [row, col]